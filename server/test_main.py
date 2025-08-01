from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_summary_action():
    response = client.post(
        "/mcp",
        json={
            "action": "predict",
            "model": "summarizer",
            "input": "This is a long test email that should be summarized.",
        },
    )
    assert response.status_code == 200
    assert "summary" in response.json()
