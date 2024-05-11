#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)
# restart flask server with flask run in server dir
@app.route('/')
def index():
    host = request.headers.get('Host')
    return f'<h1>The host for this page is {host}</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
