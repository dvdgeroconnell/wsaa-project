# record_rest_srv.py
#
# Create a basic rest server.
# See README for curl commands to test.
#
# David O'Connell

from flask import Flask, jsonify, url_for, request, redirect, abort
#from recordDAOframework import recordDAO
from recordDAO import recordDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
    return "hello"

# Get all records
@app.route('/records', methods=['GET'])
def get_all():
    # Get the response object
    return jsonify(recordDAO.get_all_records())

# Get record by ID
@app.route('/records/<int:id>', methods=['GET'])
def find_by_id(id):
    # Get the response object
    return jsonify(recordDAO.find_record_by_id(id))

# Create a record
@app.route('/records', methods=['POST'])

def create():
    # Read the JSON from the body of the incoming request
    record = {}
    record_string = request.json
    
    # build the record to create - check each field is present
    if "title" not in record_string:
        abort(400)
    record["title"] = record_string["title"]

    if "artist" not in record_string:
        abort(400)
    record["artist"] = record_string["artist"]

    if "year" not in record_string:
        abort(400)
    record["year"] = record_string["year"]

    if "genre" not in record_string:
        abort(400)
    record["genre"] = record_string["genre"]

    # Create the record, get the response object
    print("Creating", record)
    return jsonify(recordDAO.create_record(record))


# Update a record
@app.route('/records/<int:id>', methods=['PUT'])

def update(id):
    # Read the JSON from the body of the incoming request
    record = {}
    record_string = request.json

    # Build the update
    if "title" in record_string:
        record["title"] = record_string["title"]
    if "artist" in record_string:
        record["artist"] = record_string["artist"]
    if "year" in record_string:
        record["year"] = record_string["year"]
    if "genre" in record_string:
        record["genre"] = record_string["genre"]

    # Update the record, get the response object
    print("Updating record", id, "to", record)
    return jsonify(recordDAO.update_record(id, record))


# Delete a record
@app.route('/records/<int:id>', methods=['DELETE'])

def delete(id):
    # Delete the record, get the response object
    return jsonify(recordDAO.delete_record(id))

if __name__ == "__main__":
    app.run(debug=True)
