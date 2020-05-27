"""
Simple flask hello world app.  

To run put this in terminal:
export FLASK_APP=app.py
flask run
"""

# import libraries jsonify displays json
from flask import Flask, jsonify
# start flask application
app = Flask(__name__)

# creates route localhoust '/'
@app.route('/')
# create a response for the request that came to '/'
def hello_world():
    # return string
    return "Hello World!"

# create route '/hithere'
@app.route('/hithere')
# create a response for the request that came to '/hithere'
def hi_there():
    return "I just hit /hithere"

# create route for '/bye'
@app.route('/bye')
# create a response for the request that came to '/bye'.
def bye():
    # can also return python 
    retJson = {
        'field1' : 'abc',
        'field2' : 'def'
    }
    return jsonify(retJson)

    


if __name__=="__main__":
    app.run()

'''
All data sent across the internet is text.
TEXT TCP

json is a format for a data interchange between browsers and servers.
'''