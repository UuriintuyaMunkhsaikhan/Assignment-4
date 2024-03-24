from flask import Flask, render_template


fla = Flask(__name__)

@fla.route('/')
def home():
    return render_template('home.html')

@fla.route('/information')
def information():
    return render_template('information.html')

@fla.route('/data collection')
def data_collection():
    return render_template('data collection.html')

if __name__ == '__main__':
    fla.run()