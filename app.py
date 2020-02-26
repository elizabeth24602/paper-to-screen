import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'book_manager'
app.config["MONGO_URI"] = ('mongodb+srv://Elizabeth24602:gavroche24602@myfirstcluster-xtdqk.mongodb.net/book_manager?retryWrites=true&w=majority')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_book')
def get_book():
    return render_template("forum1.html", book=mongo.db.book.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)