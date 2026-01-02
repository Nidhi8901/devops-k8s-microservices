from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "Backend is running"})

@app.route("/products")
def products():
    return jsonify([
        {"id": 1, "name": "Laptop"},
        {"id": 2, "name": "Mobile"},
        {"id": 3, "name": "Headphones"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
