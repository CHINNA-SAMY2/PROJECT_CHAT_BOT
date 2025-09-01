from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend to call backend

@app.route("/", methods=["GET"])
def home():
    return "Flask chatbot backend is running! 🚀"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    # Example logic
    if "hello" in user_message.lower():
        bot_response = "Hello there! 👋"
    elif "how are you" in user_message.lower():
        bot_response = "I'm good! How are you?"
    else:
        bot_response = "Hmm... I didn't quite get that."

    return jsonify({"reply": bot_response})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
