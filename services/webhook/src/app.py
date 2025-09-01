from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend (HTML/JS) to call backend

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    # Dummy AI response for now (you can integrate AWS Lex or Cohere later)
    if "hello" in user_message.lower():
        bot_response = "Hi there! How can I help you today?"
    elif "bye" in user_message.lower():
        bot_response = "Goodbye! Have a nice day."
    else:
        bot_response = f"You said: {user_message}"

    return jsonify({"reply": bot_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
