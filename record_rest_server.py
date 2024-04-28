# record_rest_server.py
#
# Create a basic rest server.
#
# David O'Connell

from flask import Flask, url_for, request, redirect, abort

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
    return "hello"

@app.route('/test')
def test():
    return "hello from /test"
if __name__ == "__main__":
    app.run(debug=True)