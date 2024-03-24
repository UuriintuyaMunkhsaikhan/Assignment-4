from flask import Flask, render_template, request, redirect
from forms import DataCollectionForm


app = Flask(__name__, instance_relative_config=True)

app.config['SECRET_KEY'] = '123'

@app.route('/')
def home():
    return render_template('home.html')
#
@app.route('/information')
def information():
    return render_template('information.html')

@app.route('/successful')
def successffful():
    return render_template('successful.html')


@app.route('/data_collection', methods=['GET', 'POST'])
def data_collection():
    form = DataCollectionForm()
    if form.validate_on_submit():
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        gender = request.form['gender']
        student_number = request.form['student_number']
        email = request.form['email']
        answer = request.form['answer']
        grades = request.form['grades']
        satisfaction = request.form['satisfaction']
        improvements = request.form['improvements']

        data = f"First Name: {first_name}\nLast Name: {last_name}\nGender: {gender}\nStudent Number: {student_number}\nEmail: {email}\nAnswer: {answer}\nGrades: {grades}\nSatisfaction: {satisfaction}\nImprovements: {improvements}\n\n"

        with open('form_data.txt', 'a') as file:
            file.write(data)
        return redirect('/successful')
    return render_template('data_collection.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)