import sys
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        'version': sys.version
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)
