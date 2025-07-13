from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_ai_response(user_input):
    """
    Function to generate AI response based on user input.
    Replace this with your actual LLM integration.
    """
    # For now, return a simple response
    if not user_input.strip():
        return "Please enter a message."
    
    # Simple responses for demonstration
    user_input_lower = user_input.lower()
    
    if "hello" in user_input_lower or "hi" in user_input_lower:
        return "Hello! I'm here to help you with AI solutions. What can I assist you with today?"
    elif "services" in user_input_lower:
        return "We offer various AI services including machine learning, natural language processing, computer vision, and predictive analytics. Which area interests you most?"
    elif "pricing" in user_input_lower or "cost" in user_input_lower:
        return "Our pricing depends on the specific AI solution you need. Please contact us for a customized quote based on your requirements."
    elif "contact" in user_input_lower:
        return "You can reach us at contact@aicompany.com or call us at (555) 123-4567. We're here to help!"
    elif "bye" in user_input_lower or "goodbye" in user_input_lower:
        return "Thank you for chatting with us! Feel free to reach out anytime for AI solutions."
    else:
        return f"Thanks for your message: '{user_input}'. I'm here to help with any questions about our AI services. How can I assist you today?"

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
        ai_response = get_ai_response(user_message)
        ai_response = "life is cool"
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