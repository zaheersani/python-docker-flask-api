from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_datetime():
    """Endpoint to fetch the current date and time."""
    now = datetime.now()
    return jsonify({
        'current_datetime': now.strftime('%Y-%m-%d %H:%M:%S')
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
