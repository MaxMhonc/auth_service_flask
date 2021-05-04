from tests.unit.api.mock_data.users_mock_data import (
    GET_USERS_SUCCESS,
    GET_USER_SUCCESS
)


def test_users_success(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert response.get_json() == GET_USERS_SUCCESS


def test_user_get_success(client):
    user_id = 'bbc3e3b3-fe98-4fab-a5ae-b153c9c8cc9c'
    response = client.get(f'/users/{user_id}')
    assert response.status_code == 200
    assert response.get_json() == GET_USER_SUCCESS


def test_user_post_success(client):
    payload = {
        "email": "testuser@mail",
        "psw": "ffks;ldfks;ldc;ewkfpswc"
    }
    response = client.post(f'/users', json=payload)
    assert response.status_code == 201
    assert response.get_json() == {
        'message': f'User: testuser@mail created successfully'
    }


def test_user_put_success(client):
    user_id = 'bbc3e3b3-fe98-4fab-a5ae-b153c9c8cc9c'
    payload = {
        "email": "newmail@mail.com",
        "psw": "ffks;ldfks;ldc;ewkfpswc",
        "role": [
            "be807485-11bd-45a4-b3f1-ccb97d8d7c33",
        ]
    }
    response = client.patch(f'/users/{user_id}', json=payload)
    assert response.status_code == 200
    assert response.get_json() == {
        'message': f'user bbc3e3b3-fe98-4fab-a5ae-b153c9c8cc9c '
                   f'updated successfully'
    }


def test_user_patch_success(client):
    user_id = 'bbc3e3b3-fe98-4fab-a5ae-b153c9c8cc9c'
    payload = {
        "psw": "ffks;ldfks;ldc;ewkfpswc",
        "role": [
            "be807485-11bd-45a4-b3f1-ccb97d8d7c33",
        ]
    }
    response = client.patch(f'/users/{user_id}', json=payload)
    assert response.status_code == 200
    assert response.get_json() == {
        'message': f'user bbc3e3b3-fe98-4fab-a5ae-b153c9c8cc9c '
                   f'updated successfully'
    }


def test_user_delete_success(client):
    user_id = 'bbc3e3b3-fe98-4fab-a5ae-b153c9c8cc9c'
    response = client.delete(f'/users/{user_id}')
    assert response.get_json() == {
        'message': f'user bbc3e3b3-fe98-4fab-a5ae-b153c9c8cc9c '
                   f'deleted successfully'
    }
