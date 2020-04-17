from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def homePage():
    return '<H1>Hello World</H1>'

@app.route('/entry')
def entryPage():
    return render_template('entry.html', title='Compose New Entry')

## This is to allow us to run on debug mode directly with python command line.
if __name__ == '__main__':
    app.run(debug=True)
