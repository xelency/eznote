from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    return '<H1>Hello World</H1>'
