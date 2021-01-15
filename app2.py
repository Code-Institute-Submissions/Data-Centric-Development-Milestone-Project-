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

# Function to Edit Review
@app.route("/edit_review", methods=["POST"])
def edit_review():
    isbn = request.form.get('isbn')
    review_id = request.form.get('id')
    review = Reviews.find_one({'_id': ObjectId(review_id)})

    return render_template("edit.html", review=review, isbn=isbn)

# Function to Update Review
@app.route("/update_review", methods=["POST"])
def update_review():
    review_id = request.form.get('id')
    old_review = Reviews.find_one({'_id': ObjectId(review_id)})

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
    review_id = request.form.get('id')
    isbn = request.form.get('isbn')
    Reviews.delete_one({'_id': ObjectId(review_id)})

    return redirect(url_for('book', isbn=isbn))
