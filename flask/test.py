from users import *
from flask import Flask, render_template, request, session
import os
from sqlalchemy import * 

#session = {}
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def main():
	Id = Users.query.filter(Users.user_name=='abhro').first().id
	session["id"] = Id

@app.route("/hi")
def home():	
	Id = session["id"]
	print(f"Id is {Id}")


if __name__=="__main__":
	with app.app_context():
		home()