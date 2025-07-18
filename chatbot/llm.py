from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_KEY = os.getenv("GEMINI_KEY")
# Initialize model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    api_key=GEMINI_KEY,
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)


if __name__ == "__main__":
    # Simple input loop
    print("Chat with Gemini! Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = llm.invoke(user_input)
        print("Gemini:", response.content)
