import re
from flask import Flask,request,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy.model import Model
from werkzeug.utils import redirect

app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///login.sqllite3"
db=SQLAlchemy(app)
auth=HTTPBasicAuth

class User:
    def __init__(self,email,password):
        self.email=email
        self.password=password

Users=[User("test","password")]

# class User(db.Model):
#     id=db.Column('id',db.Integer,primary_key=True)
#     email = db.Column(db.String(100))
#     password = db.Column(db.String(100))
#     def __init__(self,email,password) -> None:
#         self.email=email
#         self.password=password

@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")

@auth.verify_password
def validate(email,password):
    if (User(email,password) in Users): return True


@app.route("/login",methods=["GET"])
def login():
    if(request.method=="GET"):
        return render_template("login.html")
    elif(request.method=="POST"):
        email=request.form["email"]
        password=request.form["password"]
        if(validate(email,password)):
            return redirect(url_for("success.html"))
        return "Wrong User"



@auth.login_required
@app.route("/",methods=["GET"])
def success():
    return render_template("success.html")

if(__name__=="__main__"):
    # db.create_all()
    app.run(host="localhost",port="5050")
