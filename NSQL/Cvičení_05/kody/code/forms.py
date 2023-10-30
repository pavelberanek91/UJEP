from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, TextAreaField, SubmitField, FileField
from wtforms import validators


class ContactForm(FlaskForm):
   username = StringField("User Name:",[validators.DataRequired("Please enter your name.")])
   review = TextAreaField("Review: ", [validators.DataRequired("Please enter website review.")])
   image = FileField(validators=[FileRequired()])
   submit = SubmitField("Send")

class SheepForm(FlaskForm):
   sheepname = StringField("Sheep Name:",[validators.DataRequired("Please enter sheep name.")])
   submit = SubmitField("Send")