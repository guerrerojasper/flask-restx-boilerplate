from app.models import User

def test_get_users(client):
    """
        Test GET /users endpoint
    """
    response = client.get('/users/')
    assert response.status_code == 200
    assert response.json == []

def test_create_user(client):
    """
        Test POST /user endpoint
        Test DB USER Query
    """
    new_user = {
        'name': 'testing',
        'email': 'testing@gmail.com'
    }
    response = client.post('/users/', json=new_user)
    assert response.status_code == 201
    assert response.json['name'] == 'testing'
    assert response.json['email'] == 'testing@gmail.com'

    # Veryfy if user is added to DB
    user = User.query.filter_by(name='testing').first()
    assert user is not None
    assert user.email == 'testing@gmail.com'

def test_user_with_invalid_data(client):
    """
        Test POST /user with invalid data
    """
    invalid_user = {}
    response = client.post('/users/', json=invalid_user)
    assert response.status_code == 400 # Bad request
    assert 'message' in response.json
    