from flask import Flask

#creating an instance of the flask class and give it a name 'app'
app = Flask(__name__)

#create a route using the @app.route to trigger function based on endpoint
@app.route("/")
def index():
    return "hello this is the index route"

@app.route('/posts')
def posts():
    return 'Hi this is the posts page'