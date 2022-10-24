from app import app

#create a route using the @app.route to trigger function based on endpoint
@app.route("/")
def index():
    return "hello this is the index route"

@app.route('/posts')
def posts():
    return 'Hi this is the posts page'