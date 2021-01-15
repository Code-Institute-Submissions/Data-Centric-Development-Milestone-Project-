#Review Functions to create, retrieve, update and delete records in MongoDB
@app.route("/submit_review", methods=["POST"])
def submit_review():
    isbn = request.form.get('isbn')
    review = {'username': request.form.get('username'),
              'comments': request.form.get('review'),
              'ISBN': isbn,
              'rating': int(request.form.get('rating'))}
    Reviews.insert_one(review)
    return redirect(url_for('book', isbn=isbn))
