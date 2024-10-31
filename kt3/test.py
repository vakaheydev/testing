import pytest

from kt3.base_request import BaseRequest


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
    assert get['email'] == 'test@test.tt'
    assert get['userStatus'] == 0
    print(get)


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


def test_get_store(req):
    get = req.get("store/inventory", "")
    # assert get['sold'] == 5
    assert get != None
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


@pytest.fixture
def req():
    url = 'https://petstore.swagger.io/v2'
    return BaseRequest(url)
