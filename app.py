import os
import requests

# Flask imports
from flask import Flask, render_template, request, url_for, redirect
from flask_pymongo import PyMongo

from bson.objectid import ObjectId

if os.path.exists('secrets.py'):
    import secrets

app = Flask(__name__)

app.config['MONGODB_NAME'] = os.environ.get('MONGODB_NAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

#Define method to check if a path exists - used for error handling
def exists(path):
    r = requests.head(path)
    return r.status_code == 200  # pylint: disable=no-member
#False positive with pylint (known issue)

#Define Search function to GET information from OpenLibrary API
def search_result(search_text):
    resp = requests.get(
        url='http://openlibrary.org/search.json?q=' + search_text)
    result = resp.json()

#Get results from API in JSON format
    search = result['docs']
    result_list = []
#Sort results in loop to collect 16 items and store them in an object
#Added static image to handle any book without covers
    i = 0
    alt_image = "/static/images/na.png"
    for item in search:
        if (i == 16):
            break
        isbn = item.get('isbn')
        if isbn is None:
            continue
        isbn = isbn[0]
        i += 1
        authors = item.get('author_name')
        if len(authors) > 3:
            authors = authors[:4]
        image = 'http://covers.openlibrary.org/b/isbn/{}-M.jpg'.format(isbn)
        if exists(image):
            image = alt_image
        obj = {
            "title": item.get('title'),
            "author": "".join(authors),
            'isbn': isbn,
            'image': image,
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
        book_results = search_result(search_text)
        flag = 0
        if(len(book_results) > 0):
            flag = 1
        return render_template("results.html", book_results=book_results,
                               flag=flag)

# Display singular book information as selected by User from Results page

@app.route("/book/<isbn>")
def book(isbn):
    Reviews = mongo.db.reviews
    url = "https://openlibrary.org/api/books?bibkeys=ISBN:{}".format(
        isbn) + "&format=json&jscmd=data"
    resp = requests.get(url=url)
    info = resp.json()
# commm
    info = info['ISBN:{}'.format(isbn)]
    authors = []
    publishers = []
    subjects = []
    if info.get('authors'):
        for item in info.get('authors'):
            authors.append(item.get('name'))
    if info.get('publishers'):
        for item in info.get('publishers'):
            publishers.append(item.get('name'))
    if info.get('subjects'):
        for item in info.get('subjects'):
            subjects.append(item.get('name'))
    review_list = []

    get_reviews = Reviews.find({'ISBN': isbn})
    for review in get_reviews:
        review_list.append(review)

# Find any existing reviews in MongoDB
#    get_reviews = Reviews.find({'ISBN': isbn})
#    for review in get_reviews:
#        review_list.append(review)

# Get image for selected book

    image = info.get('cover')
    if image:
        image = image.get('medium')
    else:
        image = "/static/images/na.png"
    return render_template("book.html", book=info, reviews=review_list,
                           isbn=isbn, image=image, authors="".join(authors),
                           publishers=",".join(publishers), subjects=","
                           .join(subjects))

#Review Functions to create, retrieve, update and delete records in MongoDB
@app.route("/submit_review", methods=["POST"])
def submit_review():
    Reviews = mongo.db.reviews
    isbn = request.form.get('isbn')
    review = {'username': request.form.get('username'),
              'comments': request.form.get('review'),
              'ISBN': isbn,
              'rating': request.form.get('rating')}
    Reviews.insert_one(review)
    return redirect(url_for('book', isbn=isbn))

# Function to Edit Review
@app.route("/edit_review", methods=["POST"])
def edit_review():
    Reviews = mongo.db.reviews
    isbn = request.form.get('isbn')
    review_id = request.form.get('id')
    review = Reviews.find_one_or_404({'_id': ObjectId(review_id)})

    return render_template("edit.html", review=review, isbn=isbn)

# Function to Update Review
@app.route("/update_review", methods=["POST"])
def update_review():
    Reviews = mongo.db.reviews
    review_id = request.form.get('id')
    old_review = Reviews.find_one_or_404({'_id': ObjectId(review_id)})

    isbn = request.form.get('isbn')
    print(request.form)
    new_review = {'$set': {'username': request.form.get('username'),
                           'comments': request.form.get('review'),
                           'ISBN': isbn,
                           'rating': request.form.get('rating')}}
    Reviews.find_one_and_update(
        old_review, new_review)
    return redirect(url_for('book', isbn=isbn))

# Function to Delete Review
@app.route("/delete_review", methods=["POST"])
def delete_review():
    Reviews = mongo.db.reviews
    review_id = request.form.get('id')
    isbn = request.form.get('isbn')
    Reviews.delete_one({'_id': ObjectId(review_id)})

    return redirect(url_for('book', isbn=isbn))


if __name__ == "__main__":
    app.run(debug=True)
