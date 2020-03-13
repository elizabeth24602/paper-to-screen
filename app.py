from os import path
if path.exists("env.py"):
    import env


import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'book_manager'
app.config["MONGO_URI"] = ('mongodb+srv://Elizabeth24602:Gavroche24602@myfirstcluster-xtdqk.mongodb.net/book_manager?retryWrites=true&w=majority')

mongo = PyMongo(app)

@app.route('/')
@app.route('/index1')
def index():      
    return render_template("index1.html") 
    
@app.route('/about1')
def about():      
    return render_template("about1.html") 

@app.route('/choices1')
def choices():      
    return render_template("choices1.html") 

@app.route('/forum1')
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
    
@app.route('/edit_book/<book_id>')
def edit_book(book_id):
    the_book =  mongo.db.book.find_one({"_id": ObjectId(book_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('editbook.html', book=the_book,
                           categories=all_categories)
                           
@app.route('/update_book/<book_id>', methods=["POST"])
def update_book(book_id):
    tasks = mongo.db.book
    tasks.update( {'_id': ObjectId(book_id)},
    {
        'task_name':request.form.get('task_name'),
        'category_name':request.form.get('category_name'),
        'task_description': request.form.get('task_description'),
        'star_rating': request.form.get('star_rating'),
        'is_urgent':request.form.get('is_urgent')
    })
    return redirect(url_for('get_book'))
    
@app.route('/delete_book/<book_id>')
def delete_task(book_id):
    mongo.db.tasks.remove({'_id': ObjectId(book_id)})
    return redirect(url_for('get_book'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)