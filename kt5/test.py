import pprint

import pytest
import requests


class BaseRequest:
    def __init__(self, base_url):
        self.base_url = base_url
        # set headers, authorisation etc

    def _request(self, url, request_type, data=None):
        if request_type == 'GET':
            response = requests.get(url)
        elif request_type == 'POST':
            if data is None:
                response = requests.post(url)
            else:
                response = requests.post(url, json=data)
        elif request_type == 'PUT':
            response = requests.put(url, json=data)
        elif request_type == 'DELETE':
            response = requests.delete(url)
        else:
            raise ValueError(f'No such request type: {request_type}')

        # log part
        pprint.pprint(f'{request_type} example')
        # pprint.pprint(response.url)
        pprint.pprint(response.status_code)
        # pprint.pprint(response.reason)
        # pprint.pprint(response.text)
        # pprint.pprint(response.json())
        # pprint.pprint('**********')
        return response

    def get(self, endpoint, endpoint_id, expected_error=False):
        url = self.resolve_url(endpoint, endpoint_id)
        response = self._request(url, 'GET')
        return response.json()

    def post(self, endpoint, endpoint_id, body):
        url = self.resolve_url(endpoint, endpoint_id)
        response = self._request(url, 'POST', data=body)
        return response.json()

    def post_no_body(self, endpoint, endpoint_id):
        url = self.resolve_url(endpoint, endpoint_id)
        response = self._request(url, 'POST')
        return response.json()

    def put(self, endpoint, endpoint_id, body):
        url = self.resolve_url(endpoint, endpoint_id)
        response = self._request(url, 'PUT', data=body)
        return response.status_code

    def delete(self, endpoint, endpoint_id):
        url = self.resolve_url(endpoint, endpoint_id)
        response = self._request(url, 'DELETE')
        return response.json()

    def resolve_url(self, endpoint, endpoint_id):
        return f'{self.base_url}/{endpoint}/{endpoint_id}'


# <------- USER -------> #
def test_user_post_with_list(req):
    post_data = [{
        "id": 1,
        "username": "new_test",
        "firstName": "new_test",
        "lastName": "new_test",
        "email": "new_test@test.tt",
        "password": "new_test",
        "phone": "new_test",
        "userStatus": 3
    }, {
        "id": 2,
        "username": "new_test2",
        "firstName": "new_test2",
        "lastName": "new_test2",
        "email": "new_test2@test.tt",
        "password": "new_test2",
        "phone": "new_test2",
        "userStatus": 4
    }]

    post = req.post('user/createWithList', '', post_data)
    assert post['code'] == 200
    print(post)


def test_user_post(req):
    post_data = {
        "id": 0,
        "username": "test",
        "firstName": "test",
        "lastName": "test",
        "email": "test@test.tt",
        "password": "test",
        "phone": "test",
        "userStatus": 0
    }

    post = req.post('user', '', post_data)
    assert post['code'] == 200
    print(post)


def test_user_get(req):
    get = req.get('user', 'test')
    assert get['username'] == 'test'
    assert get['userStatus'] == 0
    print(get)


def test_user_put(req):
    put_data = {
        "id": 0,
        "username": "test",
        "firstName": "test_put",
        "lastName": "test_put",
        "email": "test_put@test.tt",
        "password": "test_put",
        "phone": "test_put",
        "userStatus": 0
    }

    put_status_code = req.put('user', 'test', put_data)
    assert put_status_code == 200
    print(put_status_code)


def test_user_delete(req):
    delete = req.delete('user', 'test')
    assert delete['code'] == 200
    assert delete['message'] == 'test'
    print(delete)


def test_user_post_with_array(req):
    post_data = [{
        "id": 1,
        "username": "new_test",
        "firstName": "new_test",
        "lastName": "new_test",
        "email": "new_test@test.tt",
        "password": "new_test",
        "phone": "new_test",
        "userStatus": 3
    }, {
        "id": 2,
        "username": "new_test2",
        "firstName": "new_test2",
        "lastName": "new_test2",
        "email": "new_test2@test.tt",
        "password": "new_test2",
        "phone": "new_test2",
        "userStatus": 4
    }]

    post = req.post('user/createWithArray', '', post_data)
    assert post['code'] == 200
    print(post)


def test_user_login(req):
    user_login = req.get('user', 'login')
    print(user_login)


def test_user_logout(req):
    user_login = req.get('user', 'logout')
    print(user_login)


# <------- STORE -------> #

def test_get_store(req):
    get = req.get("store/inventory", "")
    assert get is not None
    print(get)


def test_post_store(req):
    post = req.post('store', 'order',
                    {"id": 1, "petId": 11, "quantity": 111, "shipDate": "2024-10-28T12:23:10.818Z",
                     "status": "placed", "complete": True})
    assert post['id'] == 1
    print(post)


def test_post_store_order(req):
    post = req.post('store/order', '',
                    {"id": 1, "petId": 11, "quantity": 111, "shipDate": "2024-10-28T12:23:10.818Z", "status": "placed",
                     "complete": True})
    assert post['id'] == 1
    print(post)


def test_get_store_order(req):
    get = req.get('store/order', '1')
    assert get['id'] == 1
    print(get)


# <------- PET -------> #

def test_pet_upload_image(req):
    post = req.post_no_body('pet', '2/uploadImage')
    assert post['code'] == 200
    print(post)


def test_pet_post(req):
    post_data = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    post = req.post('pet', '', post_data)
    print(post)


def test_pet_put(req):
    put_data = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    post = req.put('pet', '', put_data)
    print(post)


def test_pet_get_by_status(req):
    get = req.get('pet', 'findByStatus')
    print(get)


def test_pet_get_by_pet_id(req):
    get = req.get('pet', '1')
    print(get)


def test_pet_post_by_pet_id(req):
    post = req.post_no_body('pet', '1')
    # printervkluchite(post)


def test_pet_delete(req):
    delete = req.delete('pet', '1')
    print(delete)


@pytest.fixture
def req():
    url = 'https://petstore.swagger.io/v2'
    return BaseRequest(url)
