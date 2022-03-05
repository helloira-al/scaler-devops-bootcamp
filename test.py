from main import app
with app.test_client() as c:
    response = c.get('/')
    assert response.data == b'Welcome!'
    assert response.status_code == 200