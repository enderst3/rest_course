"""
Simple flask hello world app.  

To run put this in terminal:
export FLASK_APP=app.py
flask run
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

if __name__=="__main__":
    app.run()