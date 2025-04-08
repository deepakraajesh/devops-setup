import pytest
from flask import Flask
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Go up one directory
from app import app  # Import your Flask app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_no_env_vars(client, monkeypatch):
    """Test when no environment variables are set."""
    monkeypatch.delenv("APP_SECRET", raising=False)  # Ensure env var is not set
    monkeypatch.delenv("SOPS_SECRET", raising=False)
    response = client.get('/')
    assert response.status_code == 200
    assert b'Secret not found' in response.data
    assert b'Sops secret not found' in response.data

def test_hello_with_env_vars(client, monkeypatch):
    """Test when environment variables are set."""
    monkeypatch.setenv("APP_SECRET", "test_app_secret")
    monkeypatch.setenv("SOPS_SECRET", "test_sops_secret")
    response = client.get('/')
    assert response.status_code == 200
    assert b'test_app_secret' in response.data
    assert b'test_sops_secret' in response.data