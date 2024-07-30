import requests
import pytest
import allure

@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('Ping Tests')
@allure.title('Health Check Test')
@allure.description('Test to check the health of the booking service.')
@allure.severity(allure.severity_level.MINOR)
def test_health_check():
    with allure.step('Send a GET request to the health check endpoint'):
        response = requests.get('https://restful-booker.herokuapp.com/ping')

    with allure.step('Verify the response status code is 201'):
        assert response.status_code == 201, f'Expected status code 201, but got {response.status_code}'

