from os import path
if path.exists("env.py"):
    import env


import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'book_manager'
app.config["MONGO_URI"] = ('mongodb+srv://Elizabeth24602:Gavroche24602@myfirstcluster-xtdqk.mongodb.net/book_manager?retryWrites=true&w=majority')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_book')
def get_book():
    return render_template("forum1.html", book=mongo.db.book.find())
    
@app.route('/add_book')
def add_book():
    return render_template('addbook.html',
                            categories=mongo.db.categories.find())

@app.route('/insert_book', methods=['POST'])
def insert_book():
    tasks = mongo.db.book
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_book'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)