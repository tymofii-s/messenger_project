from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # Додано CORS
import json
import os

app = Flask(__name__)
CORS(app)  # Дозволяє CORS для всіх маршрутів

MESSAGES_FILE = "messages.json"

def load_messages():
    if os.path.exists(MESSAGES_FILE):
        with open(MESSAGES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_messages(messages):
    with open(MESSAGES_FILE, "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=4)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_messages", methods=["GET"])
def get_messages():
    return jsonify(load_messages())

@app.route("/send_message", methods=["POST"])
def send_message():
    data = request.json
    messages = load_messages()
    messages.append(data)
    save_messages(messages)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
