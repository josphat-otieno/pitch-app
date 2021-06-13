from flask import render_template
from . import main
from .. import db

@main.route('/')
def index():
    '''
    view page root function that return the index page and its data
    '''
    title = "This is your chanche to change your life"
    return render_template('index.html', title=title)
