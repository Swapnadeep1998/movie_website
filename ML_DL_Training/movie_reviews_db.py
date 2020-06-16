import sqlite3


db = sqlite3.connect("Movie_reviews.db")

cr = db.cursor()

cr.execute('''CREATE TABLE movies_feedback(Date DATE NOT NULL, Time text NOT NULL,Movie Name text NOT NULL, Ratings INT NOT NULL,
           Reviews text NOT NULL, Sentiment text Not Null)''')


db.commit()
db.close()