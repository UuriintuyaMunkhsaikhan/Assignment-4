from flask import Flask, render_template, request, redirect
from forms import DataCollectionForm
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email

app = Flask(__name__, instance_relative_config=True)

app.config['SECRET_KEY'] = '1234'

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


@app.route('/')
def home():
    return render_template('home.html')
#
@app.route('/information')
def information():
    return render_template('information.html')

@app.route('/successful')
def succeffful():
    return render_template('successful.html')

# Define a route to handle form submissions
@app.route('/data_collection', methods=['GET', 'POST'])
def data_collection():
    form = DataCollectionForm()
    if form.validate_on_submit():
        return redirect('/successful')
    return render_template('data_collection.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)