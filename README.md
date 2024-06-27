# LLM Development Suggestions API

This API is designed to analyze conversations between users using a large language model (LLM) and suggest improvements or developments based on the interaction. The implementation uses Python with the Flask or FastAPI framework and is deployed on AWS using the Serverless Framework.

## Features

- **Conversation Reception**: The API accepts a JSON containing a dialogue between a user and an LLM.
- **LLM Processing**: Processes conversations using an LLM simulation to extract insights and suggestions.
- **Return of Suggestions**: Returns suggestions based on the analysis of the conversations in JSON format.

## Technologies Used

- **Python**: Programming language.
- **Flask/FastAPI**: Framework for creating APIs.
- **AWS Lambda and API Gateway**: For hosting and managing the API.
- **Serverless Framework**: Facilitates deployment on AWS.

## Project Structure

```
project
├── app.py            # Main Flask/FastAPI application file
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
   git clone <repository-url>
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Local Execution

To run the API locally, execute:
```bash
# If using Flask
flask run

# If using FastAPI
uvicorn app:app --reload
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
  - ANY - https://h4uso9qs4f.execute-api.us-east-1.amazonaws.com/dev/
  - ANY - https://h4uso9qs4f.execute-api.us-east-1.amazonaws.com/dev/{proxy+}
- **Function Name**: project-test-dev-api
- **Function Size**: 67 MB

## Additional Documentation

- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- [Serverless Framework Documentation](https://www.serverless.com/framework/docs/)
- [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)