from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

        # "id": 1,
        # "author": "Elon Musk",
        # "date": "12/4/22",
        # "tweet": "Anything anyone says will be used against me in a court of law",
        # "likes": 504_000,

class NewTweetForm(FlaskForm):
    author = StringField('Author', validators=[DataRequired()])
    tweet = StringField('Tweet', validators=[DataRequired()])
    submit = SubmitField('Post Tweet')
