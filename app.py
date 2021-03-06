import email
import json
from flask import Flask, jsonify, request
from flask_cors import CORS

from pymongo import MongoClient
client = MongoClient(
    'mongodb+srv://turtlegram_hyun:gvSqX2om2UrFgQfU@cluster0.lh7vh.mongodb.net/cluster0?retryWrites=true&w=majority')
db = client.dbturtlegram

email = {
    'email': ' ',
}
db.email.insert_one(email)

password = {
    'password': ' ',
}
db.password.insert_one(password)

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})


@app.route("/")
def hello_world():
    return jsonify({'message': 'success'})


@app.route("/signup", methods=["POST"])
def sign_up():
    data = json.loads(request.data)
    print(data.get('email'))
    print(data["password"])

    return jsonify({'message': 'success2'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
