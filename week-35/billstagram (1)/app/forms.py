from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, StringField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    image = FileField('Image', validators=[DataRequired()])
    caption = StringField("Caption", validators=[DataRequired()])
    submit = SubmitField('Upload')