from flask import Flask

#creating an instance of the flask class and give it a name 'app'
app = Flask(__name__)

#import all of the routes from the routes module in the current folder
from . import routes