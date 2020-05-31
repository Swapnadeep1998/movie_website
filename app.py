from sentiment_app import *
from recommend import *
import sqlite3
import warnings
warnings.filterwarnings("ignore")
import datetime as dt

#Taking Inputs From The End User
name = input(str("Name of the movie: "))
ratings = int(input("Rate this movie: "))
review = input(str("Give your reviews: ")) 
          
#Defining Function To Insert Datas Into Database Table
def insert_into_db(name,ratings,review,r_sentiment):
    date = str(dt.datetime.now())
    date,_ = date.split(".")
    date,time = date.split()

    db = sqlite3.connect('Movie_reviews.db')
    cr = db.cursor()
    
    cr.execute('''INSERT INTO movies_feedback(Date,Time,Movie, Ratings, Reviews, Sentiment)
                   VALUES(?,?,?,?,?,?);''',(date,time,name,ratings,review,r_sentiment))
    db.commit()
    db.close()
    return
    
#Defining The Final Application Model Function
def model(name,ratings,review):
    if get_similar_movies(name, ratings):
        print(get_similar_movies(name, ratings))
        r_sentiment = "Positive" if sentiment(list(review))[0][0] >0.5 else "Negative"
        insert_into_db(name,ratings,review,r_sentiment)
        print(r_sentiment)
        

model(name,ratings,review)