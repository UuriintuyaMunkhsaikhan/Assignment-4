from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email

class DataCollectionForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    gender = RadioField('Gender', choices=[('male', 'Male'), ('female', 'Female'), ('they/them', 'They/Them'), ('prefer-not-to-say', 'Prefer Not to Say')], validators=[DataRequired()])
    student_number = StringField('Student Number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    answer = RadioField('Do you think Student clubs and society is efficient?', choices=[('yes', 'Yes'), ('no', 'No'), ('idk', "I don't know")], validators=[DataRequired()])
    grades = StringField('Grades')
    satisfaction = SelectField('Overall Satisfaction with Academic Experience', choices=[('excellent', 'Excellent'), ('good', 'Good'), ('average', 'Average'), ('poor', 'Poor')], validators=[DataRequired()])
    improvements = TextAreaField('Suggestions for Improvement', validators=[DataRequired()])

