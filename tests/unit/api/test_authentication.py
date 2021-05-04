def test_registration_success(client):
    response = client.post('/registration')
    assert response.status_code == 201
    assert response.get_json() == {
            'endpoint': 'registration/',
            'request_method': 'POST',
            'status': 'not implemented'
        }


def test_sign_in_success(client):
    response = client.post('/sign-in')
    assert response.status_code == 200
    assert response.get_json() == {
            'endpoint': 'sign-in/',
            'request_method': 'POST',
            'status': 'not implemented'
        }


def test_sign_out_success(client):
    response = client.post('/sign-out')
    assert response.status_code == 200
    assert response.get_json() == {
            'endpoint': 'sign-out/',
            'request_method': 'POST',
            'status': 'not implemented'
        }


def test_refresh_success(client):
    response = client.post('/refresh')
    assert response.status_code == 200
    assert response.get_json() == {
            'endpoint': 'refresh/',
            'request_method': 'POST',
            'status': 'not implemented'
        }
