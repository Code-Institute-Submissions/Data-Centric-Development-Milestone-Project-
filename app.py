# Flask imports
from flask import Flask, render_template, request, url_for, redirect
from flask_pymongo import PyMongo

# Create Flask instance
app = Flask(__name__)

#Define MONGO URI with Credentials/DB
app.config['MONGO_URI'] = 'mongodb+srv://root:70AoSLdgfRWWrOE6@myfirstcluster.w2rzj.mongodb.net/reviewdb?retryWrites=true&w=majority'
mongo = PyMongo(app)
Reviews = mongo.db.reviews

import requests
from bson.objectid import ObjectId

#Define Search function to GET information from OpenLibrary API
def search_result(search_text):
    resp = requests.get(
        url='http://openlibrary.org/search.json?q=' + search_text)
    result = resp.json()
