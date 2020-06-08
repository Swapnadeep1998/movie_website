from sentiment_app import *
from recommend import *
from users import *
from flask import Flask, render_template, request, session
import os
from sqlalchemy import * 


app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def home():
    return render_template("about.html")

@app.route("/login", methods = ["POST","GET"])
def login():
    return render_template("login.html")

@app.route("/signup", methods = ["POST","GET"])
def signup():
    return render_template("register.html")

@app.route("/login_results", methods = ["POST","GET"])
def login_results():
    session["user_name"] = request.form.get('Name')
    session["password"] = request.form.get('Password')

    #Flight.query.filter(and_(Flight.origin == "Paris", Flight.duration > 500)).all()
    count = Users.query.filter(and_(Users.user_name == session["user_name"],Users.password == session["password"])).all()
    if len(count)==1: 
        return render_template("movies.html")             
    else:
        message = "You are not registered, Please register yourself"
        return render_template("error.html", message = message)
    
    

@app.route("/register_results", methods = ["POST","GET"])
def register_results():
    user_name = request.form.get("Name")
    password = request.form.get("Password")
    confirm = request.form.get("Confirm")
    if password==confirm:
        count = Users.query.filter_by(user_name = user_name).count()
        if count==0:
            register = Users(user_name = user_name, password = password)
            db.session.add(register)
            db.session.commit()
            #message = "User Registration Successful"
            return render_template("login.html")
        else:
            message = "Error, User Name Already Exists"
            return render_template("error.html", message = message)
    else:
        message = "You have'nt entered same password in repeat password section"
        return render_template("error.html", message = message)
    


@app.route("/movies", methods = ["POST","GET"])
def movies():
    if request.method == "POST":        
        movie_name = request.form.get("Name")
        ratings = request.form.get("Ratings")
        reviews = request.form.get("Reviews")
        items = get_similar_movies(movie_name, int(ratings))      
        senti = sentiment([reviews])
        Sentiment = "Positive" if senti>0.5 else "Negative"
        user_name = session["user_name"]
        user_id = Users.query.filter(Users.user_name==user_name).first().id        
        movies = Movies(user_id=user_id,movie_name=movie_name,ratings=ratings,reviews=reviews,sentiment=Sentiment)
        db.session.add(movies) 
        db.session.commit()       
        return render_template("movies.html", items= items, senti = Sentiment)                
    return render_template("movies.html")
                         
if __name__=="__main__":
    with app.app_context():
        app.run(debug = True)
