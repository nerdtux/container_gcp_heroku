from flask import Flask
from flask_cors import CORS
from os import environ


app = Flask(__name__)

CORS(app)

@app.route('/')
def index():
    service = environ.get('SERVICE', 'SERVICE DEFAULT')
    return f'<h1>{service}</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(environ.get('PORT', 5000)))