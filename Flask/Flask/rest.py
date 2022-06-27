import pymysql
from app import app
from db import mysql
from flask import jsonify, request

@app.route('/unites')
def unites():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM unite")
    rows = cursor.fetchall()
    resp = jsonify(rows)
    resp.status_code = 200
    return resp 

@app.route('/automates')
def automates():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM automate")
    rows = cursor.fetchall()
    resp = jsonify(rows)
    resp.status_code = 200
    return resp 

@app.route('/donnee_mesuree')
def donnee_mesuree():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM donnee_mesuree")
    rows = cursor.fetchall()
    resp = jsonify(rows)
    resp.status_code = 200
    return resp 

@app.route('/fichier')
def fichier():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM fichier")
    rows = cursor.fetchall()
    resp = jsonify(rows)
    resp.status_code = 200
    return resp    


@app.route('/getAutomateById')
def getIdAutomateByRef():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    ref = request.args.get('ref')
    uniteId = request.args.get('uniteId')

    try:
        cursor = mysql.cursor()
        sql="SELECT id FROM automate WHERE reference_type = %s AND id_unite= %d"
        val= (ref, uniteId)
        cursor.execute(sql, val)
        data = str(cursor.fetchone()[0])
        resp = data
        resp.status_code = 200
        conn.close()
        return resp 
    except Exception as e:
        print("Problem with getAutomateById : " + str(e))
        return False


@app.route('/addDatas', methods=['GET','POST'])
def addDonneeMesuree():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    if request.method == 'GET':
        return 'bad request!', 400
    if request.method == 'POST':
        try:
            request_data = request.get_json()
            valeur =  request_data['valeur']
            unite_mesure =  request_data['unite_mesure']
            date_heure =  request_data['date_heure']
            id_automate =  request_data['id_automate']
            sql="INSERT INTO donnee_mesuree (valeur, unite_mesure, date_heure, id_automate) VALUES (%d, %s, %f, %s, %s)"
            val= ( valeur, unite_mesure, date_heure, id_automate )
            cursor.execute(sql, val)
            conn.close()
        except Exception as e:
            return(str(e))



if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')