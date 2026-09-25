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
        {"id": 1, "name": "Laptop", "price": 1000},
        {"id": 2, "name": "Mobile", "price": 600},
        {"id": 3, "name": "Headphones", "price": 120}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
