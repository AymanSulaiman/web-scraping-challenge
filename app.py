from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)

@app.route("/")
def index():
    pass

@app.route("/scrape")
def scraper():
    pass

if __name == "__main__":
    app.run(Debug = True)