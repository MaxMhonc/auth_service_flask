from tests.unit.api.mock_data.roles_mock_data import (
    GET_ROLES_SUCCESS,
    GET_ROLE_SUCCESS
)


def test_roles_success(client):
    response = client.get('/roles')
    assert response.status_code == 200
    assert response.get_json() == GET_ROLES_SUCCESS


def test_role_get_success(client):
    user_id = '3b12c6ef-bb75-498c-9269-e8989762c59c'
    response = client.get(f'/roles/{user_id}')
    assert response.status_code == 200
    assert response.get_json() == GET_ROLE_SUCCESS


def test_role_post_success(client):
    payload = {
        "name": "name_4",
        "description": "Just to test how it works"
    }
    response = client.post(f'/roles', json=payload)
    assert response.status_code == 201
    assert response.get_json() == {
        'message': f'Role: name_4 created successfully'
    }


def test_role_put_success(client):
    role_id = '3b12c6ef-bb75-498c-9269-e8989762c59c'
    payload = {
        "name": "new_old_role",
        "description": "And try to add users",
        "user": [
            "bbc3e3b3-fe98-4fab-a5ae-b153c9c8cc9c",
            "aeb1c933-d5e5-4395-8e00-26404e9d6412"
        ]
    }
    response = client.patch(f'/roles/{role_id}', json=payload)
    assert response.status_code == 200
    assert response.get_json() == {
        'message': f'role 3b12c6ef-bb75-498c-9269-e8989762c59c '
                   f'updated successfully'
    }


def test_role_patch_success(client):
    role_id = '3b12c6ef-bb75-498c-9269-e8989762c59c'
    payload = {
        "description": "And try to add users",
        "user": [
            "bbc3e3b3-fe98-4fab-a5ae-b153c9c8cc9c",
            "aeb1c933-d5e5-4395-8e00-26404e9d6412"
        ]
    }
    response = client.patch(f'/roles/{role_id}', json=payload)
    assert response.status_code == 200
    assert response.get_json() == {
        'message': f'role 3b12c6ef-bb75-498c-9269-e8989762c59c '
                   f'updated successfully'
    }


def test_role_delete_success(client):
    role_id = '3b12c6ef-bb75-498c-9269-e8989762c59c'
    response = client.delete(f'/roles/{role_id}')
    assert response.get_json() == {
        'message': f'role 3b12c6ef-bb75-498c-9269-e8989762c59c '
                   f'deleted successfully'
    }
