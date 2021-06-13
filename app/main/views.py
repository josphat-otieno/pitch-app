from flask import render_template, redirect, url_for, abort, request
from . import main
from .. import db
from ..models import User, Pitch, Comments
from flask_login import login_required, current_user 
from .forms import PitchForm, CommentsForm

@main.route('/')
def index():
    '''
    view page root function that return the index page and its data
    '''
    pitches = Pitch.query.all()
    love = Pitch.query.filter_by(category = 'Love').all()
    education = Pitch.query.filter_by(category = 'Education').all()
    business = Pitch.query.filter_by(category = 'Business').all()
    interview = Pitch.query.filter_by(category = 'Interview').all()
    promotion = Pitch.query.filter_by(category = 'Promotion').all()
    title = "This is your chanche to change your life"
    return render_template('index.html', title=title, pitches = pitches, education = education, love = love, business = business, interview = interview, promotion = promotion)

