# wsaa-project
Repository for the WSAA CY24 final project.

## Overview
This project implements a database of a catalogue of LP records.

## Files in this Repository

#### recordDAOframework.py
DAO framework with a set of stubs for development and test purposes.

#### README.md
This file.


## API Definition
The parameters are:

ID - the ID that the program assigns to the entry
Title - the name of the record
Artist - the artist / band featuring on the record
Year - the year the record was released
Genre - The type of music, e.g. Jazz, Rock, Prog, Folk, Punk, Disco

The API will implement the following operations:

| Operation | Method | URL | Sample Parameters | Sample Responses |
|-----------|--------|-----|-------------------|------------------|
| Get All | GET | /records | None | [{...},{...},{...}] |
| Find by ID | GET | /records/id | None | {"id":"1", "Title" : "xxx", |
| | | | | "Artist":"xxx", "Year":1973,|
| | | | | "Genre":"Rock"} |
| Create | POST | /records | {"Title" : "xxx", | {"id":"1", "Title" : "xxx", |
| | | |  "Artist":"xxx", "Year":1973, | "Artist":"xxx", "Year":1973,|
| | | |  "Genre":"Rock"} | "Genre":"Rock"} |
| Update | PUT | /records/id | e.g. {"Year":1970} | {"id":"1", "Title" : "xxx", |
| | | | | "Artist":"xxx", "Year":1970,|
| | | | | "Genre":"Rock"} |
| Delete | DELETE | /records/id | None | {"done":True} |

As the program will be implemented in stages, curl will be used to test the server-side functionality.

### Sample CURL commands
Following commands are used with the web server running on localhost.

#### Get All
curl -X GET http://127.0.0.1:5000/records

#### Find by ID
5 is just an example, and can be changed.
curl -X GET http://127.0.0.1:5000/records/5

#### Create
curl -X POST -H "Content-Type: application/json" -d "{\"title\":\"Closer\", \"artist\":\"Joy Division\", \"year\":1981, \"genre\":\"post punk\"}" http://127.0.0.1:5000/records

#### Update
curl -X PUT -H "Content-Type: application/json" -d "{\"title\":\"Further\"}" http://127.0.0.1:5000/records/5

#### Delete 
curl -X DELETE http://127.0.0.1:5000/records/5
