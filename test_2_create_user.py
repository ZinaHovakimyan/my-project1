import pytest
import requests
import allure


@pytest.mark.smoke
class TestPostUser():

    @allure.title("Test POST /users API endpoint")
    @allure.description("This test verifies that a POST request to the /users endpoint creates a new user with the specified name and job.")
    def test_create_user(self):
        data = {
            "name": "morpheus",
            "job": "leader"
        }
        headers = {'Content-Type': 'application/json'}

        with allure.step("Send POST request to create a new user"):
            response = requests.post(
                'https://reqres.in/api/users',
                json=data,
                headers=headers
            )

        with allure.step("Verify the response status code is 201"):
            assert response.status_code == 201, "Status code is incorrect"

    @allure.title("Test successful registration with valid credentials")
    @allure.description("This test verifies that a POST request to the /register endpoint successfully registers a user with valid email and password, and that a token is returned in the response.")
    def test_register_successful(self):
        data = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        headers = {'Content-Type': 'application/json'}

        with allure.step("Send POST request to /register with valid credentials"):
            response = requests.post(
                'https://reqres.in/api/register',
                json=data,
                headers=headers
            )

        with allure.step("Verify the response status code is 200"):
            assert response.status_code == 200, "Status code is incorrect"

        with allure.step("Verify the 'token' field in the response is not empty"):
            assert response.json().get('token') is not None, 'The token is empty'

    @allure.title("Test successful login with valid credentials")
    @allure.description("This test verifies that a POST request to the /login endpoint successfully logs in a user with valid email and password, and that a token is returned in the response.")
    def test_login_successful(self):
        data = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        headers = {'Content-Type': 'application/json'}

        with allure.step("Send POST request to /login with valid credentials"):
            response = requests.post(
                'https://reqres.in/api/login',
                json=data,
                headers=headers
            )

        with allure.step("Verify the response status code is 200"):
            assert response.status_code == 200, "Status code is incorrect"

        with allure.step("Verify the 'token' field in the response is not empty"):
            assert response.json().get('token') is not None, 'The token is empty'

    @allure.title("Test registration with missing password")
    @allure.description("This test verifies that a POST request to the /register endpoint returns a 400 status code and the appropriate error message when the password field is missing.")
    def test_negative_register(self):
        data = {
            "email": "sydney@fife"
        }
        headers = {'Content-Type': 'application/json'}

        with allure.step("Send POST request to /register with missing password"):
            response = requests.post(
                'https://reqres.in/api/register',
                json=data,
                headers=headers
            )

        with allure.step("Verify the response status code is 400"):
            assert response.status_code == 400, "Status code is incorrect"

        with allure.step("Verify the error message indicates missing password"):
            assert response.json().get(
                'error') == "Missing password", f'The error received is {response.json().get("error")}'

    @allure.title("Test login with missing password")
    @allure.description("This test verifies that a POST request to the /login endpoint returns a 400 status code and the appropriate error message when the password field is missing.")
    def test_login_unsuccessful(self):
        data = {
            "email": "peter@klaven"
        }
        headers = {'Content-Type': 'application/json'}

        with allure.step("Send POST request to /login with missing password"):
            response = requests.post(
                'https://reqres.in/api/login',
                json=data,
                headers=headers
            )

        with allure.step("Verify the response status code is 400"):
            assert response.status_code == 400, "Status code is incorrect"
