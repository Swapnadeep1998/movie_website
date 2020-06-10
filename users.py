from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()


#database movie_app
#export DATABASE_URL="postgresql:///movie_app"
class Users(db.Model):
	__tablename__ = "users_data"
	id = db.Column(db.Integer, primary_key = True)
	user_name = db.Column(db.String(25), unique = True, nullable=False)
	password = db.Column(db.String, nullable=False)

class Movies(db.Model):
	__tablename__ = "movie_data"
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey("users_data.id"), nullable=False)
	movie_name = db.Column(db.String, nullable=False)	
	ratings = db.Column(db.Integer, nullable=False)
	reviews = db.Column(db.String, nullable = False)
	sentiment = db.Column(db.String, nullable=False)

class Scores(db.Model):
	__tablename__ = "scores_py"
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey("users_data.id"), nullable=False)
	score = db.Column(db.Integer, nullable=False, default=0)

						
