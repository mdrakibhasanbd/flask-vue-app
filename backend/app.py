from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

@app.route('/api/v1/test', methods=['GET'])
def test_api():
    return jsonify({"message": "Hello from Flask API!", "status": "success"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5008)
