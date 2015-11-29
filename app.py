# pylint: disable=broad-except,invalid-name
"""
    Sample Flask app testing Cassandra connection
"""
import os
from datetime import datetime
from flask import Flask, jsonify, redirect, url_for

from cassandra.cluster import Cluster
from cassandra.query import ordered_dict_factory

app = Flask(__name__)

@app.route('/')
def index():
    """ root index redirects to test function """
    return redirect(url_for('test'))

@app.route('/test')
def test():
    """ Try to establish Cassandra connection and return simple query results """
    cluster = Cluster([os.environ.get('CASSANDRA_PORT_9042_TCP_ADDR', 'localhost')],
                      port=int(os.environ.get('CASSANDRA_PORT_9042_TCP_PORT', 9042))
                     )
    try:
        session = cluster.connect()
    except Exception as error:
        message = "%s: %s" % (error.__class__.__name__, str(error))
        return jsonify(message=message, hostname=os.uname()[1],
                       current_time=str(datetime.now())), 500
    session.row_factory = ordered_dict_factory
    rows = session.execute('SELECT * FROM system.schema_keyspaces LIMIT 10')
    return jsonify(data=rows, hostname=os.uname()[1],
                   current_time=str(datetime.now()))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
