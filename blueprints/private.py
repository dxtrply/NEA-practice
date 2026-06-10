from flask import Blueprint, app, redirect, render_template, session
from database import DatabaseHandler
from libary.isAuthed import isAuthed

private = Blueprint("private",__name__)
db = DatabaseHandler()

@private.before_request
def privateGate():
    if not isAuthed():
        return redirect("/")

@private.route ("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@private.route ("/signout")
def signout():
    #get rid of session data
    session.clear()
    #send user back to the sign in page
    return redirect("/")

@private.route("/addTask")
def addTask():
    return render_template("addTask.html")
