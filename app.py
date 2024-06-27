from flask import Flask, request, jsonify, make_response
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def hello_from_root():
    return jsonify(message='Hello from root!')

@app.route("/hello")
def hello():
    return jsonify(message='Hello from path!')

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    if not data or "conversation" not in data:
        return make_response(jsonify(error="Invalid input!"), 400)

    conversation = data["conversation"]
    messages = [{"role": item["role"], "content": item["content"]} for item in conversation]

    try:
        # Make OpenAI API call
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        # Extract suggestions (for example purposes, taking the first response)
        suggestions = response.choices[0].message.content
    except Exception as e:
        return make_response(jsonify(error=str(e)), 500)

    return jsonify(suggestions=suggestions)

@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)

if __name__ == "__main__":
    app.run(debug=True)
