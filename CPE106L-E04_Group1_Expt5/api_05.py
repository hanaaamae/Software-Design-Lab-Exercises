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

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/api/v1/resources/albums', methods=['GET'])
def api_filter():
    query_parameters = request.args

    id = query_parameters.get('albumid')
    title = query_parameters.get('title')
    
    query = "SELECT * FROM albums WHERE"
    to_filter = []

    if id:
        query += ' albumid=? AND'
        to_filter.append(id)
    if title:
        query += ' title=? AND'
        to_filter.append(title)    
    if not (id or title):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('chinook.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)



app.run()

