from flask_wtf import FlaskForm
from wtforms.validators import Required
from wtforms import StringField, SubmitField, TextAreaField,validators




class PitchForm(FlaskForm):
    title = StringField("Title", validators=[Required])
    # category = SelectField("Category", choices=[('Love','Love'),('Education','Education'),('Business','Business'),('Interview', 'Interview'),('Promotion', 'Promotion'), validators=[Required]])
    pitch = TextAreaField('Write your Pitch', validators=[Required])
    submit = SubmitField('Pitch')

class CommentsForm(FlaskForm):
    comment = TextAreaField('Leave your comment', validators = [Required])
    submit = SubmitField("Comments")

class UpdateProfile(FlaskForm):
    bio = TextAreaField("Tell us about yourslef.", validators=[Required()])  
    submit = SubmitField('Submit')
