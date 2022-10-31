from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login


# Create a User class that inherits from the db.Model class
# CREATE TABLE user(id SERIAL PRIMARY KEY, email VARCHAR(50) UNIQUE NOT NULL, etc.)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(50), nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Set the password to the hashed version of the password
        self.password = self.set_password(kwargs.get('password', ''))
        # Add and commit the new instance to the database
        db.session.add(self)
        db.session.commit()

    def __str__(self):
        return self.username

    def set_password(self, plain_password):
        return generate_password_hash(plain_password)

    def check_password(self, password_guess):
        return check_password_hash(self.password, password_guess)


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# Create a Post Model - One to Many relationship with User (one user to many posts, one post to one user)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # SQL equivalent to FOREIGN KEY(user_id) REFERENCES user(id)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<Post {self.id} | {self.title}>"


    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key in {'title','body'}:
                setattr(self, key, value)
        db.session.commit()


#delete post from database
    