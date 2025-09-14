from fastapi.testclient import TestClient
from mainv2 import app_v2

client = TestClient(app_v2)

def test_positive_sentiment():
    response = client.post("/v1/sentiment", json={"text": "Det var en god lærer."})
    assert response.status_code == 200
    score=response.json()
    return score

def test_negative_sentiment():
    response = client.post("/v1/sentiment", json={"text": "It was a bad course."})
    assert response.status_code == 200
    score=response.json()
    return score

if __name__ == "__main__":
    score_pos=test_positive_sentiment()
    score_neg=test_negative_sentiment()
    print(score_pos)
    print(score_neg)
    print("All tests passed!")