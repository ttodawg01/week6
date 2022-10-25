from flask import render_template
from app import app
from app.forms import SignUpForm

# Create routes for our app
@app.route('/')
def index():
    user_info = {
        'username': 'cbale',
        'email': 'christianb@movies.com'
    }
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    return render_template('index.html', user=user_info, colors=colors)


@app.route('/posts')
def posts():
    return render_template('posts.html')


@app.route('/signup')
def signup():
    form = SignUpForm()
    return render_template('signup.html', form=form)