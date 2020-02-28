import redis
from flask import Flask
app = Flask(__name__)

r = redis.Redis(host='redis')

@app.route('/set/<key>/<value>')
def set(key, value):
    r.set(key, value)
    return "success"

@app.route('/get/<key>')
def get(key):
    return r.get(key)


