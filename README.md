# LLM Development Suggestions API

This API is designed to analyze conversations between users and a large language model (LLM) to suggest improvements based on the interaction. The implementation uses Python with the Flask framework and is deployed on AWS using the Serverless Framework.

## Features

- **Conversation Reception**: The API accepts a JSON containing a dialogue between a user and an LLM.
- **LLM Processing**: Processes conversations using an LLM to extract insights and suggestions.
- **Return of Suggestions**: Returns suggestions based on the analysis of the conversations in JSON format.

## Technologies Used

- **Python**: Programming language.
- **Flask**: Framework for creating APIs.
- **AWS Lambda and API Gateway**: For hosting and managing the API.
- **Serverless Framework**: Facilitates deployment on AWS.

## Project Structure

```
project
├── app.py            # Main Flask application file
├── requirements.txt  # Project dependencies
├── serverless.yml    # Configuration for Serverless Framework deployment
├── package.json      # Node.js package configuration
├── package-lock.json # Node.js package lock file
└── README.md         # Project documentation
```

## Configuration and Execution

### Prerequisites

- Python 3.8+
- AWS CLI configured with administrator credentials
- Serverless Framework

### Local Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/tsnthiago/mentora-ai.git
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Local Execution

To run the API locally, execute:
```bash
flask run
```

### Deploy on AWS

To deploy on AWS using the Serverless Framework, execute:
```bash
serverless deploy
```

## API Usage

### Endpoint

`POST /analyze`

### Request Body

```json
{
  "conversation": [
    {"role": "user", "content": "User talks about the 1:1"},
    {"role": "assistant", "content": "LLM responds about the 1:1"},
    {"role": "user", "content": "User talks more about the 1:1"},
    {"role": "assistant", "content": "LLM responds again"}
  ]
}
```

### Expected Response

```json
{
  "suggestions": ["Suggestion 1", "Suggestion 2", "Suggestion 3"]
}
```

## Deployment Details

After successful deployment, the following details were provided:
- **Service Name**: project-test
- **Stage**: dev
- **Region**: us-east-1
- **Endpoint URLs**:
  - ANY - https://blzhgjxr8d.execute-api.us-east-1.amazonaws.com/dev
  - ANY - https://blzhgjxr8d.execute-api.us-east-1.amazonaws.com/dev/{proxy+}
- **Function Name**: project-test-dev-api
- **Function Size**: 67 MB

## Testing

### Using Postman

To test the API using Postman, follow these steps:
1. Open Postman and create a new POST request.
2. Set the request URL to `https://blzhgjxr8d.execute-api.us-east-1.amazonaws.com/dev/analyze`.
3. In the "Body" tab, select "raw" and "JSON" and enter the following JSON:
   ```json
   {
     "conversation": [
       {"role": "user", "content": "Olá, estou me preparando para minha primeira reunião 1:1 com meu gerente. O que devo focar?"},
       {"role": "assistant", "content": "É ótimo que você esteja se preparando. Nas reuniões 1:1, é importante discutir seus objetivos de carreira, feedback recente e qualquer obstáculo que você esteja enfrentando no trabalho."},
       {"role": "user", "content": "Entendi. Devo trazer exemplos específicos de projetos em que estou trabalhando?"},
       {"role": "assistant", "content": "Sim, definitivamente. Trazer exemplos específicos pode ajudar a ilustrar seus pontos e mostrar seu progresso. Além disso, pode ser uma boa oportunidade para pedir feedback sobre esses projetos."}
     ]
   }
   ```
4. Click "Send" to receive the suggestions in the response.

### Running Tests

To run the tests, execute:
```bash
pytest
```

## Additional Documentation

- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- [Serverless Framework Documentation](https://www.serverless.com/framework/docs/)
- [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)