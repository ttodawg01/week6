from flask import render_template
from app import app

#create a route using the @app.route to trigger function based on endpoint
@app.route("/")
def index():
    user_info = {
        'username':'tonyc',
        'email':'tonycampos@gmail.com',
    }
    colors = ['red', 'orange', 'blue']
    return render_template('index.html', user=user_info, colors = colors)

@app.route('/posts')
def posts():
    return 'Hi this is the posts page'