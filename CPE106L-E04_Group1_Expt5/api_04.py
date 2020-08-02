import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Accessing Chinook Database</h1>
<p>A prototype API for accessing the chinook sqlite sample database.</p>'''



@app.route('/api/v1/resources/albums/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('chinook.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM albums;').fetchall()

    return jsonify(all_books)

app.run()

