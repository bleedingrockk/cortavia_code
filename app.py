from flask import Flask, render_template, request, jsonify
from chatbot.main import interact_with_llm

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")
        
        # Get AI response
        ai_response = interact_with_llm(user_message)
        print(ai_response)
        return jsonify({
            "success": True,
            "response": ai_response
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)