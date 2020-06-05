from sentiment_app import *
from recommend import *
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods = ["POST","GET"])
def index():
    if request.method == "POST":        
        name = request.form.get("Name")
        ratings = request.form.get("Ratings")
        review = request.form.get("Reviews")
        items = get_similar_movies(name, int(ratings))
        senti = sentiment([review])
        senti = "Positive" if senti>0.5 else "Negative"         
        return render_template("index.html", items= items, senti = senti)                
    return render_template("index.html")
                         
if __name__=="__main__":
    app.run(debug=True)
