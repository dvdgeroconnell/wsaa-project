# record_rest_srv.py
#
# Create a basic rest server.
#
# David O'Connell

from flask import Flask, url_for, request, redirect, abort

import mysql

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
    return "hello"

# Get all records
@app.route('/records', methods=['GET'])
def getall():
    return "get all"

# Get record by ID
@app.route('/records/<int:id>', methods=['GET'])
def findbyid(id):
    return "find by id"

# Create a record
@app.route('/records', methods=['POST'])
def create():
    # read json from the body
    record_string = request.json
    return f"create {record_string}"

# Update a record
@app.route('/records/<int:id>', methods=['PUT'])
def update(id):
    record_string = request.json
    return f"update {id} {record_string}"

# Delete a record
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    return f"delete {id}"

if __name__ == "__main__":
    app.run(debug=True)

# CURL commands to test
# Get All
# curl http://127.0.0.1:5000/records
# find by ID
# curl http://127.0.0.1:5000/records/1
# Create
# curl -X POST -H "Content-Type: application/json" -d "{\"title\":\"Closer\", \"artist\":\"Joy Division\", \"price\":699}" http://127.0.0.1:5000/records
# Update
# curl -X PUT -H "Content-Type: application/json" -d "{\"title\":\"Closer\", \"artist\":\"Joy Division\", \"price\":1099}" http://127.0.0.1:5000/records/1
# Delete
# curl -X DELETE http://127.0.0.1:5000/records/1