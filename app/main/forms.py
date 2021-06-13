from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, TextAreaField
from wtforms import validators
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField("Title", validators=[Required])
    category = SelectField("Category", choices=[('Love','Love'),('Education','Education'),('Business','Business'),('Interview', 'Interview'),('Promotion', 'Promotion')], validators=[Required])
    pitch = TextAreaField('Write your Pitch', validators=[Required])
    submit = SubmitField('Pitch')

class CommentsForm(FlaskForm):
    comment = TextAreaField('Leave your comment', validators = [Required])
    submit = SubmitField("Comments")