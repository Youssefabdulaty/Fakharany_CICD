from flask
import Flask, jsonify

app = Flask(__name__)
@app.route('/yasser', methods=['GET'])
def get_yasser():
    return jsonify({"message": "Hello from Yasser!"})   


if __name__ == "__main__":
    app.run(debug=True)