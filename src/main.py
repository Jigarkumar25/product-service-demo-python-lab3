from flask import Flask, jsonify
from flask_cors import CORS
import os

# Initialize Flask app
app = Flask(__name__)

# Enable CORS (Cross-Origin Resource Sharing)
CORS(app, resources={r"/products": {"origins": "*"}})

# Get port from environment variable (default: 3030)
PORT = int(os.environ.get("PORT", 3030))

# Define route for /products
@app.route("/products", methods=["GET"])
def get_products():
    products = [
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99}
    ]
    return jsonify(products)

# Start the Flask server
if __name__ == "__main__":
    # host="0.0.0.0" allows external access (important for Azure)
    app.run(host="0.0.0.0", port=PORT)
