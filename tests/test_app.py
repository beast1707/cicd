from app import app

def test_home_status_code():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_home_content():
    client = app.test_client()
    response = client.get('/')
    assert b"Welcome" in response.data or b"CI/CD" in response.data

def test_health_endpoint():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    assert b"ok" in response.data or b"status" in response.data
