from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id: db.Column(db.Integer, primary_key=True)
    title: db.Column(db.String(100), nullable=False)
    content: db.Column(db.Text, nullable=False)
    author: db.Column(db.String(20), nullable=False, default='N/A')
    date_posted: db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'Blog Post '+ str(self.id)

all_posts = [
    {
        'title': 'Post One',
        'content': 'This is the content of the post one',
        'author': 'Azhari'
    },
    {
        'title': 'Post Two',
        'content': 'This is the content of the post two'
    },
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html', posts=all_posts)

@app.route('/home/users/<string:name>/posts/<int:id>')
def hello(name, id):
    return 'Hello, '+name +' your id is: '+ str(id)

@app.route('/onlyget', methods=['GET'])
def get_req():
    return 'this page is GET'

if __name__ == '__main__':
    app.run(debug=True)