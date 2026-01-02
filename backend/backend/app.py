from flask import Flask, jsonify
from flask_cors import CORS   # <--- import CORS

app = Flask(__name__)
CORS(app)  # <--- allow all origins

products = [
    {"name": "Product A", "price": 10},
    {"name": "Product B", "price": 20}
]

@app.route("/products")
def get_products():
    return jsonify(products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
