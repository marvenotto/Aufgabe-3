from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = "data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.route("/person", methods=["POST"])
def create_person():
    data = request.get_json()
    name = data.get("name")
    db = load_data()
    db[name] = data
    save_data(db)
    return jsonify({"message": f"Person {name} created"}), 201

@app.route("/person/<name>", methods=["PUT"])
def update_email(name):
    data = request.get_json()
    email = data.get("email")
    db = load_data()
    if name in db:
        db[name]["email"] = email
        save_data(db)
        return jsonify({"message": f"Email for {name} updated"}), 200
    return jsonify({"error": "Person not found"}), 404

@app.route("/", methods=["GET"])
def index():
    return jsonify(load_data())

if __name__ == "__main__":
    app.run()
