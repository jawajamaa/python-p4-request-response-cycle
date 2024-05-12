#!/usr/bin/env python3

import os

from flask import Flask, current_app, g, make_response, request

app = Flask(__name__)

@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name
    response_body =  f'''
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
        <h3>The path of this application on the user's device is {g.path}</h3>'''
    
    status_code = 200
    headers = {}

    return make_response(response_body, status_code, headers)

# below is 'normal?' approach; above is the more OOP code and easier to reuse.  Both show same lines in browser
# @app.route('/')
# def index():
#     host = request.headers.get('Host')
#     appname = current_app.name
#     return f'''<h1>The host for this page is {host}</h1>
#                 <h2>The name of this application is {appname}</h2>
#                 <h3>The path of this application on the user's device is {g.path}</h3>'''

if __name__ == '__main__':
    app.run(port=5555, debug=True)
