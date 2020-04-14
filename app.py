from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars as s_m

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_data"
mongo = PyMongo(app)

@app.route("/")
def index():
    pass

@app.route("/scrape")
def scraper():
    pass

if __name__ == "__main__":
    app.run(Debug = True)