from flask import Blueprint, app, flash, redirect, render_template, request, session
from database import DatabaseHandler
from libary.isAuthed import isAuthed
from libary.isValidLength import isValidLength

private = Blueprint("private",__name__)
db = DatabaseHandler()

@private.before_request
def privateGate():
    if not isAuthed():
        return redirect("/")

@private.route ("/dashboard")
def dashboard():
    username = session.get("currentUser")
    success, tasks = db.readALLTasks(username)

    if not success:
        flash("failed to fetch tasks")
        return redirect("/dashboard") #<-- worried about this!
    
    return render_template("dashboard.html", tasks = tasks)

    


@private.route ("/signout")
def signout():
    #get rid of session data
    session.clear()
    #send user back to the sign in page
    return redirect("/")

@private.route("/addTask", methods = ["POST","GET"])
def addTask():
    if request.method == "POST":
        formData = request.form
        description = formData.get("description")
        username = session.get("currenUser")

        if username == None:
            flash("No user found ")
            return redirect*("/addTask")

        if not isValidLength(description, 2):
            flash("Invalid Description")
            return redirect("/addTask")
        
        success, message = db.createTasks(description,  )
        if not success:
            flash(message)
            return redirect("/addTask")
        
        flash(message)
        return redirect("/dashboard")
    
    return render_template("addTask.html")
