import pytest
import requests
import allure


@allure.feature('TEST UPDATE AND DELETE USER - feature')
@allure.suite('TEST UPDATE AND DELETE USER - suite')
@pytest.fixture()
def create_user():
    data = {
             "name": "morpheus",
             "job": "leader"
            }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://reqres.in/api/users',
        json=data,
        headers=headers
    )
    new_id = response.json()['id']
    yield new_id

@allure.title('Update User Partially Test')
@allure.description('Test case to partially update a user')
@pytest.mark.regression
def test_update_user_partial(create_user):
        data = {
                "updatedAt": "2024-07-14T12:37:18.698Z"
                }
        headers = {'Content-Type': 'application/json'}

        response = requests.patch(
            'https://reqres.in/api/users/{new_id}',
            json=data,
            headers=headers
            )

        with allure.step("Verify status code is 200"):
            assert response.status_code == 200, 'Status code is incorrect'



@allure.title('Update User Test')
@allure.description('Test case to update a user with new name and job')
@pytest.mark.regression
def test_update_user(create_user):
    data = {
            "name": "zina morpheus",
            "job": "hov zion resident",
            "updatedAt": "2024-07-14T13:30:38.675Z"
            }
    headers = {'Content-Type': 'application/json'}

    response = requests.put(
        'https://reqres.in/api/users/{new_id}',
        json=data,
        headers=headers
    )

    with allure.step("Send PUT request to update user with new name and job"):
        assert response.status_code == 200, 'Status code is incorrect'


@allure.title('Delete User Test')
@allure.description('Test case to delete a user with new name and job')
@pytest.mark.regression
def test_delete_user(create_user):
    response = requests.delete(f'https://reqres.in/api/users/{"new_id"}')
    with allure.step("Send DELETE request to delete user with new name and job"):
        assert response.status_code == 204, 'Status code is incorrect'
