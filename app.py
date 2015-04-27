# import the Flask class from the flask module
from flask import Flask, render_template

from content_management import content

TOPIC_DICT = content()


# create the application object
app = Flask(__name__)


# use decorators to link the function to a url
@app.route('/')
def home():
    title = "Pineapple"
    paragraph = "NYC City Bike tour. Discovering NYC by bike."
    return render_template('index.html', title=title, paragraph=paragraph)


@app.route('/about')
def welcome():
    return render_template('about.html', TOPIC_DICT=TOPIC_DICT)


@app.route('/about/contact')
def contact():
    return render_template('contact.html')


@app.route('/tours')
def book():
    return render_template('tours.html')


@app.route('/essentials')
def essentials():
    return render_template('essentials.html')


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
