from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

@app.route('/data')
def get_data():
    conn = psycopg2.connect(
        host="db",
        database="testdb",
        user="testuser",
        password="testpass"
    )
    cur = conn.cursor()
    cur.execute("SELECT 'Hello from DB!'")
    result = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify(message=result[0])