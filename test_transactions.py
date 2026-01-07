import pytest
from fastapi.testclient import TestClient
from main import app, Base, engine

# Create tables for testing
Base.metadata.create_all(bind=engine)

client = TestClient(app)

def test_create_transaction_success():
    response = client.post("/transactions", json={"amount": 100})
    assert response.status_code == 200
    data = response.json()
    assert data["amount"] == 100
    assert data["status"] == "pending"
    assert "id" in data

def test_create_transaction_invalid_amount():
    response = client.post("/transactions", json={"amount": -10})
    assert response.status_code == 400

def test_approve_transaction():
    create = client.post("/transactions", json={"amount": 200})
    tx_id = create.json()["id"]

    approve = client.post(f"/transactions/{tx_id}/approve")
    assert approve.status_code == 200
    assert approve.json()["status"] == "approved"

def test_cannot_approve_twice():
    create = client.post("/transactions", json={"amount": 300})
    tx_id = create.json()["id"]

    client.post(f"/transactions/{tx_id}/approve")
    second_attempt = client.post(f"/transactions/{tx_id}/approve")
    assert second_attempt.status_code == 400
