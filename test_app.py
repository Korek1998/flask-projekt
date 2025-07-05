from app import app

def test_add():
    client = app.test_client()
    response = client.get('/api/add?a=2&b=3')
    assert response.status_code == 200
    assert response.json['result'] == 5

def test_square():
    client = app.test_client()
    response = client.get('/square/5')
    assert response.status_code == 200
    assert response.json['result'] == 25
