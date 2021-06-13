from flask import render_template
from . import main
from .. import db
from ..models import User, Pitch

@main.route('/')
def index():
    '''
    view page root function that return the index page and its data
    '''
    pitches = Pitch.query.all()
    title = "This is your chanche to change your life"
    return render_template('index.html', title=title, pitches=pitches)
