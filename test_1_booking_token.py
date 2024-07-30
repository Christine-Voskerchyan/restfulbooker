import requests
import pytest
import allure

# Initialize the global token variable
my_token = None

@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('Token Booking Suite')
@allure.title('Create Authentication Token')
@allure.description('Test to create and verify an authentication token from the Booking API.')
@allure.severity(allure.severity_level.CRITICAL)
def test_booking_create_token():
    data = {
        "username": "admin",
        "password": "password123"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send POST request to create token'):
        response = requests.post(
        'https://restful-booker.herokuapp.com/auth',
        json=data,
        headers=headers
    )

    with allure.step('Verify response status code'):
        assert response.status_code == 200, f'Expected status code 200 but got {response.status_code}'

    response_json = response.json()

    with allure.step('Check if token is present in response'):
        assert 'token' in response_json, 'Token not found in response'

    with allure.step('Verify token is not empty'):
        assert len(response_json['token']) > 0, 'Token is empty'


    global my_token
    my_token = response_json.get('token')

