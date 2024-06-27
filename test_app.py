import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_root(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Hello from root!' in rv.data

def test_hello(client):
    rv = client.get('/hello')
    assert rv.status_code == 200
    assert b'Hello from path!' in rv.data

def test_analyze(client):
    rv = client.post('/analyze', json={
        "conversation": [
            {"role": "user", "content": "Usuário fala sobre o 1:1"},
            {"role": "assistant", "content": "LLM responde sobre o 1:1"},
            {"role": "user", "content": "Usuário fala mais sobre o 1:1"},
            {"role": "assistant", "content": "LLM responde novamente"}
        ]
    })
    if rv.status_code != 200:
        print(f"Response data: {rv.data}")
    assert rv.status_code == 200
    assert b'suggestions' in rv.data
