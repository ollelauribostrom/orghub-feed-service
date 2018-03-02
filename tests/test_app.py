import pytest
import json
from src.app import app

@pytest.fixture
def client():
  return app.test_client()

def test_response(client):
  """Test that the app is responding"""
  res = client.get('/')
  assert res.status_code == 200

def test_root_message(client):
  """Test that root route returns a json object containing a message"""
  res = client.get('/')
  data = json.loads(res.data)
  assert data["message"] == "Feed service up and running"

def test_feed(client):
  """Test that feed route returns a list of events"""
  res = client.get('/feed/orghub-app')
  data = json.loads(res.data)
  assert type(data) is list