from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length


# This is the form used to enter new a entry for each journal
class EntryForm(FlaskForm):
	EntryDate = DateField('Date',
				validators=[DataRequired()])
	EntryTopic = StringField('Topic',
	 			validators=[DataRequired(),Length(min=2, max=50)])
	EntryBody = TextAreaField('Text Body', 
				validators=[DataRequired(),Length(min=1)])
	EntrySubmit = SubmitField('Post Entry')

