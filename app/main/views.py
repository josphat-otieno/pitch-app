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

@main.route('/create_new', methods = ['POST','GET'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user
        new_pitch_object = Pitch(post=post,user_id=current_user._get_current_object().id,category=category,title=title)
        new_pitch_object.save_p()
        return redirect(url_for('main.index'))
