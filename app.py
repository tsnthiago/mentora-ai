import os
import json
import openai

from flask import Flask, request, jsonify, make_response
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Swagger UI setup
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'  # Path to your swagger.json file
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "LLM Development Suggestions API"
    }
)

# Load Swagger spec from file
with open('swagger.json') as f:
    swagger_spec = json.load(f)

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

    # Add detailed prompt for LLM
    detailed_prompt = {
        "role": "system",
        "content": (
            "Você é um assistente de IA especializado em fornecer sugestões para melhorar conversas entre usuários "
            "e grandes modelos de linguagem. Com base na conversa a seguir, forneça sugestões acionáveis para que o usuário "
            "melhore sua interação. As sugestões devem ser práticas e voltadas para aprimorar a qualidade e a eficácia da conversa. "
            "Cada sugestão deve conter no mínimo 100 palavras. "
            "A resposta deve ser retornada no formato JSON: "
            "[\"Sugestão 1\", \"Sugestão 2\", \"Sugestão 3\"]"
        )
    }
    messages = [detailed_prompt] + [{"role": item["role"], "content": item["content"]} for item in conversation] 

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        suggestions = response.choices[0].message.content
    except openai.APIError as e:
        return make_response(jsonify(error=f"OpenAI API error: {str(e)}"), 500)
    except openai.APIConnectionError as e:
        return make_response(jsonify(error=f"Failed to connect to OpenAI API: {str(e)}"), 500)
    except openai.RateLimitError as e:
        return make_response(jsonify(error=f"OpenAI API request exceeded rate limit: {str(e)}"), 500)
    except Exception as e:
        return make_response(jsonify(error=f"Unexpected error: {str(e)}"), 500)

    return jsonify(suggestions=suggestions)

@app.route("/swagger.json")
def swagger_json():
    return jsonify(swagger_spec)

@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)
