from flask import Flask, send_file, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/api')
def api():
    res = requests.get('http://backend:5000/data')
    return jsonify(res.json())