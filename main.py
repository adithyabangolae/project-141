from flask import Flask,jsonify
import csv

all_articles = []

with open("articles.csv") as f:
    reader = csv.reader(f)
    data  = list(reader)
    all_articles  = data[1:]
    
liked_articles = []
not_liked_articles = []

app = Flask(__name__)

@app.route("/get-articles")

def get_articles():
    return jsonify({
        "data":all_articles[0],
        "status":"successful"
    })
    
@app.route("/liked-articles",methods=["POST"])

def liked_articles_function():
    articles = all_articles[0]
    liked_articles.append(articles)
    return jsonify({
        "status":"succcessful"
    }), 201
    
@app.route("/not-liked-articles",methods=["POST"])

def not_liked_articles_function():
    articles = all_articles[0]
    not_liked_articles.append(articles)
    all_articles.pop(0)
    return jsonify({
        "status":"succcessful"
    }), 201
    
if __name__ == "__main__":
    app.run()