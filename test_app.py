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
def test_home_page():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"Kalkulator Flask" in response.data

def test_add_api():
    response = app.test_client().get('/api/add?a=4&b=6')
    assert response.status_code == 200
    assert response.json['result'] == 10
