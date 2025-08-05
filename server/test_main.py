from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_summary_action():
    response = client.post(
        "/mcp",
        json={
            "action": "predict",
            "model": "summarize",
            "input": "This is a long test email that should be summarized.",
        },
    )
    assert response.status_code == 200
    assert "summary" in response.json()


def test_sentiment_action():
    response = client.post(
        "/mcp",
        json={
            "action": "predict",
            "model": "sentiment",
            "input": "I love this amazing product!",
        },
    )
    assert response.status_code == 200
    assert "sentiment" in response.json()


def test_unknown_model():
    response = client.post(
        "/mcp",
        json={
            "action": "predict",
            "model": "unknown",
            "input": "test",
        },
    )
    assert response.status_code == 200
    assert response.json() == {"error": "Unknown model"}


def test_unknown_action():
    response = client.post(
        "/mcp",
        json={
            "action": "unknown",
            "model": "summarize",
            "input": "test",
        },
    )
    assert response.status_code == 200
    assert response.json() == {"error": "Unsupported action"}
