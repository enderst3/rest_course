"""
Simple flask hello world app.  

To run put this in terminal:
export FLASK_APP=app.py
flask run
"""

# import libraries jsonify displays json
from flask import Flask, jsonify, request
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

# create route to accept post request
@app.route('/add_two_nums', methods=["POST"])
def add_two_nums():
    #get x,y from posted data
    dataDict = request.get_json()
    return jsonify(dataDict)
    
    #Add z=x+y

    #Prepare a JSON, 'z':z

    #return jsonify(map_prepared)
# create route for '/bye'
@app.route('/bye')
# create a response for the request that came to '/bye'.
def bye():
    # can also return python 
    age = 2*15
    retJson = {
        'Name': 'Todd',
        'Age': age,
        'phones':[
            {
                'phone_name': "iphone8",
                'phone_number': 12345
            },
            {
                'phone_name': "iphone6",
                'phone_number': 54321
            }
        ]
    }
    return jsonify(retJson), 404

    


if __name__=="__main__":
    app.run()

'''
All data sent across the internet is text.
TEXT TCP

json is a format for a data interchange between browsers and servers.
'''