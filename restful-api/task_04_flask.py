#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane",
             "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}


@app.route("/")
def home():
    return "Welcome to the Flask API!"[1]


@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))[2]


@app.route("/status")
def status():
    return "OK"[3]


@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])[4]
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.json
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400[5]

    username = data["username"]
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201[6]


if __name__ == "__main__":
    app.run(debug=True)
