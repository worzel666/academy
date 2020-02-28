from flask import Flask
app = Flask(__name__)

@app.route('/<text>')
def hello_world(text):
    with open('/volume', 'w') as textfile:
        textfile.write(text)
    return 'Success'
