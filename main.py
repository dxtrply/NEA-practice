from flask import Flask, flash, redirect, render_template, request
from libary.isPresent import isPresent
from libary.isValidLength import isValidLength


app = Flask(__name__)
app.secret_key = "c5jxYGkbYBylQxxx3LjdJY6db91cmmMcaHHMovBym44"


@app.route("/")
def home():
    return render_template("signup.html")

@app.route("/signup", methods = ["POST"])
def signup():

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
        return redirect("/")

    return "signing up..."


app.run(debug=True)