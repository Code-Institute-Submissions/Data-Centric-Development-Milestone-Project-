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

#Get results from API in JSON format
    search = result['docs']
    result_list = []
#Sort results in loop to collect 10 items and store them in an object
    i = 0
    for item in search:
        if (i == 10):
            break
        i += 1
        isbn = item.get('isbn')
        if isbn is not None:
            isbn = isbn[0]
        authors = item.get('author_name')
        authors = authors[:4]
        obj = {
            "title": item.get('title'),
            "author": authors,
            'isbn': isbn,
            'image': 'http://covers.openlibrary.org/b/isbn/{}-M.jpg'.format(isbn),
            #Use ISBN of selected books and pass them as arguements to COVERS API to get an image (if it exists)
        }
        result_list.append(obj)

    return result_list

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/results", methods=["POST"])
def results():
    if request.method == "POST":
        search_text = request.form['search']
        return render_template("results.html", book_results=search_result(search_text))


if __name__ == "__main__":
    app.run(debug=True)
