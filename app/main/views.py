from flask import render_template, redirect, url_for, abort, request
from . import main
from .. import db, photos
from ..models import User, Pitch, Comments,Upvote, Downvote
from flask_login import login_required, current_user 
from .forms import PitchForm, CommentsForm, UpdateProfile, UpvoteForm, DownvoteForm

@main.route('/')
@login_required
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
    upvotes = Upvote.get_all_upvotes(pitch_id=Pitch.id)    
    downvotes = Upvote.get_all_upvotes(pitch_id=Pitch.id)
    header = "This is your chanche to change your life"
    return render_template('index.html', header=header, pitches = pitches, education = education, love = love, business = business, interview = interview, promotion = promotion, upvotes=upvotes, downvotes=downvotes)


@main.route('/comment/<int:pitch_id>', methods = ['GET','POST'])
@login_required
def comment(pitch_id):
    '''
    page function to enable users comment on a pitch
    '''
    form = CommentsForm()
    pitch = Pitch.query.get(pitch_id)
    all_comments = Comments.query.filter_by(pitch_id = pitch_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        # pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        new_comment = Comments(comment = comment,user_id = user_id,pitch_id = pitch_id)
        new_comment.save_comments()

        return redirect(url_for('.comment', pitch_id = pitch_id))
    
    return render_template('comment.html', form =form, pitch = pitch,all_comments=all_comments)


@main.route('/new_pitch/new', methods = ['POST','GET'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        post_pitch = form.post_pitch.data
        category = form.category.data
        user_id = current_user
        new_pitch_object = Pitch(post_pitch=post_pitch,user_id =current_user._get_current_object().id,category=category,title=title)
        new_pitch_object.save_pitch()

        db.session.add(new_pitch)
        db.session.commit()
        return redirect(url_for('main.index'))
        
    return render_template('new_pitch.html', form = form)


@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username = name).first()
    user_id = current_user._get_current_object().id
    pitches = Pitch.query.filter_by(user_id = user_id).all()
    if user is None:
        abort(404)

  
    return render_template("profile/profile.html", user = user,pitches= pitches)

@main.route('/user/<name>/update',methods = ['GET','POST'])
@login_required
def update_profile(name):
    user = User.query.filter_by(username =name).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',name=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<name>/update/pic',methods= ['POST'])
@login_required
def update_pic(name):
    user = User.query.filter_by(username = name).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',name=name))

# @main.route('/pitch/upvote/<int:pitch_id>/upvote', methods = ['GET', 'POST'])
# @login_required
# def upvote(pitch_id):
#     upvote_form = UpvoteForm()
#     pitch = Pitch.query.get(pitch_id)
#     user = current_user
#     pitch_upvotes = Upvote.query.filter_by(pitch_id= pitch_id)
    
#     if Upvote.query.filter(Upvote.user_id==user.id,Upvote.pitch_id==pitch_id).first():
#         return  redirect(url_for('main.index'))

#     new_upvote = Upvote(pitch_id=pitch_id, user = current_user)
#     new_upvote.save_upvotes()
#     return redirect(url_for('main.index'))

#     return render_template('upvote_form.html', upvote_form=upvote_form,)

# @main.route('/pitch/downvote/<int:pitch_id>/downvote', methods = ['GET', 'POST'])
# @login_required
# def downvote(pitch_id):
#     form = DownvoteForm()
#     pitch = Pitch.query.get(pitch_id)
#     if form.validate_on_submit():
#     user= current_user
#     pitch_downvotes = Downvote.query.filter_by(pitch_id= pitch_id)
    
#     if Downvote.query.filter(Downvote.user_id==user.id,Downvote.pitch_id==pitch_id).first():
#         return  redirect(url_for('main.index'))


#     new_downvote = Downvote(pitch_id=pitch_id, user = current_user)
#     new_downvote.save_downvotes()
#     return redirect(url_for('main.index'))