from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set the database URI before initializing SQLAlchemy
DB_NAME = 'flaskaws'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://admin:Rutuja*1998@flaskaws.ctwi2sqeobc5.eu-north-1.rds.amazonaws.com/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional, but good practice to turn off

# Now initialize SQLAlchemy
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    author = db.Column(db.String(100), nullable = False)
    price = db.Column(db.Float)

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)


@app.route('/add/', methods = ['POST'])
def insert_book():
    if request.method == "POST":
        book = Book(
            title = request.form.get('title'),
            author = request.form.get('author'),
            price = request.form.get('price')
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
