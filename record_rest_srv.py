# record_rest_srv.py
#
# Create a basic rest server.
# See README for curl commands to test.
#
# David O'Connell

from flask import Flask, jsonify, url_for, request, redirect, abort
from flask_cors import CORS, cross_origin
#from recordDAOframework import recordDAO
from recordDAO import recordDAO

# Had to enable CORS headers in flask (browser - no domain or running from file)
# https://stackoverflow.com/questions/25594893/how-to-enable-cors-in-flask

app = Flask(__name__, static_url_path='', static_folder='staticpages')
cors = CORS(app) # only needed if you want to expose all routes to cross origin
app.config['CORS_HEADERS'] = 'Content-Type' # not sure if needed

#------------------------------------------------------------------------
# Index

@app.route('/')
@cross_origin()
def index():
    return {"response":"hello"}

#------------------------------------------------------------------------
# Get all records

@app.route('/records', methods=['GET'])
@cross_origin()

def get_all():
    # Get the response object
    return jsonify(recordDAO.get_all_records())

#------------------------------------------------------------------------
# Get record by ID

@app.route('/records/<int:id>', methods=['GET'])
@cross_origin()

def find_by_id(id):
    # Get the response object
    return jsonify(recordDAO.find_record_by_id(id))

#------------------------------------------------------------------------
# Create a record

@app.route('/records', methods=['POST'])
@cross_origin()

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

#------------------------------------------------------------------------
# Update a record

@app.route('/records/<int:id>', methods=['PUT'])
@cross_origin()

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

#------------------------------------------------------------------------
# Delete a record

@app.route('/records/<int:id>', methods=['DELETE'])
@cross_origin()

def delete(id):
    # Delete the record, get the response object
    if recordDAO.delete_record(id):
        return jsonify({"done":True})
        #return jsonify(recordDAO.delete_record(id))

if __name__ == "__main__":
    app.run(debug=True)