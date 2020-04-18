from flask import Flask, render_template
from forms import EntryForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'somekey'

@app.route('/')
def Page_Home():
	return render_template('home.html', title='Welcome')

@app.route('/entry')
def Page_Entry():
    return render_template('entry.html', title='Compose New Entry', form=EntryForm())

## This is to allow us to run on debug mode directly with python command line.
if __name__ == '__main__':
    app.run(debug=True)
