from flask import Flask, render_template

app = Flask(__name__)

all_posts = [
    {
        'title': 'Post One',
        'content': 'This is the content of the post one'
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