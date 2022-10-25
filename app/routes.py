from flask import render_template, redirect, url_for, flash
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


@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        print('Hooray our form submitted!')
        # Get data from form
        email = form.email.data
        username = form.username.data
        password = form.password.data
        print(email, username, password)
        # Add a new user to the database

        # Flash a success message
        flash("You have succesffuly signed up!", "success")
        # Redirect back to home
        return redirect(url_for('index'))

    return render_template('signup.html', form=form)