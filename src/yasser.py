from flask import Flask, jsonify, request

app = Flask(__name__)

# Home endpoint
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Hello from Flask API"})

# GET example
@app.route("/hello/<name>", methods=["GET"])
def hello(name):
    return jsonify({"message": f"Hello {name}"})

# POST example
@app.route("/sum", methods=["POST"])
def sum_numbers():
    data = request.json
    a = data.get("a", 0)
    b = data.get("b", 0)
    return jsonify({"result": a + b})

if __name__ == "__main__":
    app.run(debug=True)
