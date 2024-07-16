import pytest
import allure
import requests


@allure.feature("TEST GET - feature")
@allure.suite('TEST GET - suite')
@pytest.mark.regression
class TestGet():

    @allure.title("Test retrieval of user list from page 2")
    @allure.description("This test verifies that a GET request to the /users endpoint returns a 200 status code and that the response contains data when requesting users from page 2.")
    def test_get_list_users(self):
        with allure.step("Send GET request to /users endpoint for page 2"):
            response = requests.get('https://reqres.in/api/users?page=2')

        with allure.step("Verify the response status code is 200"):
            assert response.status_code == 200, "Status code is incorrect"

        with allure.step("Verify that the response data is not empty"):
            response_data = response.json().get('data', [])
            assert len(response_data) > 0, 'Data is empty'


    @allure.title("Test retrieval of a single user")
    @allure.description("This test verifies that a GET request to the /users/2 endpoint returns a 200 status code and that the response contains both 'data' and 'support' fields.")
    def test_get_a_single_user(self):
        with allure.step("Send GET request to /users/2 endpoint"):
            response = requests.get('https://reqres.in/api/users/2')

        with allure.step("Verify the response status code is 200"):
            assert response.status_code == 200, "Status code is incorrect"

        response_data = response.json()

        with allure.step("Verify the response contains 'data' field"):
            assert 'data' in response_data, "The response does not contain 'data'"

        with allure.step("Verify the response contains 'support' field"):
            assert 'support' in response_data, "The response does not contain 'support'"

    @allure.title("Test retrieval of resource list")
    @allure.description("This test verifies that a GET request to the /unknown endpoint returns a 200 status code and that the response correctly indicates the first page of resources.")
    def test_get_list_resource(self):
        with allure.step("Send GET request to /unknown endpoint"):
            response = requests.get('https://reqres.in/api/unknown')

        with allure.step("Verify the response status code is 200"):
            assert response.status_code == 200, "Status code is incorrect"

        with allure.step("Verify the response indicates page 1"):
            assert response.json().get('page') == 1, 'The page number is incorrect, expected page 1'

    @allure.title("Test retrieval of a single resource")
    @allure.description("This test verifies that a GET request to the /unknown/2 endpoint returns a 200 status code and that the response contains the correct resource name.")
    def test_single_resource(self):
        with allure.step("Send GET request to /unknown/2 endpoint"):
            response = requests.get('https://reqres.in/api/unknown/2')

        with allure.step("Verify the response status code is 200"):
            assert response.status_code == 200, "Status code is incorrect"

        with allure.step("Verify the resource name in the response data is 'fuchsia rose'"):
            assert response.json()['data']['name'] == 'fuchsia rose', 'The name is incorrect'

    @allure.title("Test retrieval of user list with delayed response")
    @allure.description("This test verifies that a GET request to the /users endpoint with a delay parameter returns a 200 status code and that the response indicates the correct page number.")
    def test_get_delayed_response(self):
        with allure.step("Send GET request to /users endpoint with a delay of 3 seconds"):
            response = requests.get('https://reqres.in/api/users?delay=3')

        with allure.step("Verify the response status code is 200"):
            assert response.status_code == 200, "Status code is incorrect"

        with allure.step("Verify that the response indicates page 1"):
            assert response.json()['page'] == 1, 'The page number is incorrect, expected page 1'

    @allure.title("Test response for a single user not found")
    @allure.description("This test verifies that a GET request to the /users/23 endpoint returns a 404 status code and an empty response body when the user does not exist.")
    def test_single_user_not_found(self):
        with allure.step("Send GET request to /users/23 endpoint"):
            response = requests.get('https://reqres.in/api/users/23')

        with allure.step("Verify the response status code is 404"):
            assert response.status_code == 404, "Status code is incorrect"

        with allure.step("Verify the response body is empty"):
            assert response.json() == {}, 'Response body should be empty'

    @allure.title("Test response for a single resource not found")
    @allure.description("This test verifies that a GET request to the /unknown/23 endpoint returns a 404 status code and an empty response body when the resource does not exist.")
    def test_single_resource_not_found(self):
        with allure.step("Send GET request to /unknown/23 endpoint"):
            response = requests.get('https://reqres.in/api/unknown/23')

        with allure.step("Verify the response status code is 404"):
            assert response.status_code == 404, "Status code is incorrect"

        with allure.step("Verify the response body is empty"):
            assert response.json() == {}, 'Response body should be empty'