from flask import Flask, jsonify, request
from flask_restful import Api, Resource

'''
Objective: Build Restful API that supports  +,-,/,*
- Methods: GET, POST, PUT, DELETE
- Resources: What you are offering.... +,-,/,*
- Need to have Method, Path, Usedfor, Parameters, status
'''


app = Flask(__name__)
api = Api(app)



@app.route('/')
def hello_world():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)
