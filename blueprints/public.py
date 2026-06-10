from flask import Blueprint,  flash, redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from database import DatabaseHandler
from libary import isAuthed
from libary.isPresent import isPresent
from libary.isValidLength import isValidLength

db = DatabaseHandler()
db.createTables()

public = Blueprint("public", __name__)

@public.before_request
def privateGate():
    if isAuthed():
        return redirect("/dashboard")




@public.route("/", methods = ["POST", "GET"])
def home():
    if request.method == "GET":
        return render_template("login.html")
    
    #return "logging in..."

    if request.method == "POST":
        formData = request.form
        username = formData.get("username")
        password = formData.get("password")
        
        success, passwordHash = db.readUserPasswordHash(username)

        if not success or passwordHash == None:
            flash("Error during lohin,please try again.")
            return redirect("/")
        
        ##check against password
        if check_password_hash(passwordHash[0], password):
                flash("invalid login details - please try again")
                return redirect("/")
        
        #success!
        session["currentUser"] = username
        return redirect("/dashboard")
    


@public.route("/signup", methods = ["POST", "GET"])
def signup():

    if request.method == "GET":
        return render_template("signup.html")

    formData = request.form
    username = formData.get("username")
    password = formData.get("password")
    repassword = formData.get("repassword")

    success = True

    if not isPresent(username):
        success = False 
        flash("No username provided. ")

    if not isValidLength(username, 4):
        success = False      
        flash("username not over 4 characters. ") 

    if not isPresent(password):
        success = False
        flash("No username provided. ")

    if not isValidLength(password, 8):
        success = False
        flash("Password must be 8 characters or more. ")
    
    if not isPresent(password):
        success = False
        flash("password not re-entered. ")

    if not isValidLength(password, 8):
        success = False
        flash("re-entered password must be 8 or more characters. ")

    if password != repassword:
        success = False
        flash("passwords do not match. ")

    if not success:
        return redirect("/signup")

    hashedPassword = generate_password_hash(password)


    db_success, message = db.createUser(username, hashedPassword)
    
    if not db_success:
        flash(message)
        return redirect("/signup")
    #successful sign up   
    session["currentUser"] = username
    return redirect("/dashboard")