from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder="../frontend")
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")
def serve_file(path):
    return send_from_directory(app.static_folder, path)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    if "hello" in user_message.lower():
        bot_response = "Hello there! 👋"
    elif "how are you" in user_message.lower():
        bot_response = "I'm good! How are you?"
    else:
        bot_response = "Hmm... I didn't quite get that."

    return jsonify({"reply": bot_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
