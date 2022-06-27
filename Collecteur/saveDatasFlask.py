from typing import List, Dict
from flask import Flask
import mysql.connector
import json
import os

app = Flask(__name__)


def test_table() -> List[Dict]:
    config = {
        'user': 'userDV',
        'password': 'password',
        'host': 'aubonbeurre_tp_datavisualisation_host',
        'port': '3366',
        'database': 'datavisubeurre'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM unite')
    results = [{name: color} for (name, color) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index() -> str:
    return json.dumps({'test_table': test_table()})
    
