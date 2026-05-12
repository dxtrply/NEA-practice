from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("signup.html")

@app.route("/signup", methods = ["POST"])
def signup():

    formData = request.form
    username = formData.get("username")
    password = formData.get("password")
    repassword = formData.get("repassword")
    print(username, password, repassword)

    return "signing up..."


app.run(debug=True)