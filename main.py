from flask import Flask, flash, redirect, render_template, request, session

from database import DatabaseHandler
from libary.isPresent import isPresent
from libary.isValidLength import isValidLength
from werkzeug.security import check_password_hash, generate_password_hash
from blueprints.public import public
from blueprints.private import private


app = Flask(__name__)
app.secret_key = "c5jxYGkbYBylQxxx3LjdJY6db91cmmMcaHHMovBym44"
db = DatabaseHandler()
db.createTables()

app.register_blueprint(public)
app.register_blueprint(private)

    
app.run(debug=True, port=6000)