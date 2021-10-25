
from flask import Flask,request,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth


app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///users.sqllite3"
app.secret_key = "TEST"
db=SQLAlchemy(app)
auth=HTTPBasicAuth()

class User(db.Model):
    id:int=db.Column("id",db.Integer,primary_key=True)
    name: str = db.Column(db.String(100))
    email:str=db.Column(db.String(100))
    password: str = db.Column(db.String(100))
    def __init__(self,name,email,password):
        self.name = name
        self.email=email
        self.password=password

@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")

@auth.verify_password
def validate(email,password):
    try:
        res=User.query.filter_by(email=email)
        if (res[0].password==password):return True
        return False
    except Exception as e:
        return False


@app.route("/login",methods=["GET","POST"])
def login():
    if(request.method=="GET"):
        return render_template("login.html")
    elif(request.method=="POST"):
        email=request.form["email"]
        password=request.form["password"]
        if(validate(email,password)):
            return redirect(url_for("success"))
        return "User does not exist please register!!"


@app.route("/success",methods=["GET"])
@auth.login_required()
def success():
    # return 'Loggedin:'+auth.current_user()
    return render_template("success.html")


@app.route("/register",methods=["GET","POST"])
def register():
    if(request.method=="GET"):
        return render_template("register.html")
    elif(request.method=="POST"):
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        user=User(name,email,password)
        db.session.add(user)
        db.session.commit()
        return ("User Created "+"\n".join(i.name for i in User.query.all()))

if(__name__=="__main__"):
    db.create_all()
    app.run(host="localhost",port="5050",debug=True)
