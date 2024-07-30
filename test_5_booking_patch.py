import requests
import pytest
import allure
import test_1_booking_token
import test_2_booking_post


@pytest.mark.regression
@pytest.mark.smoke
@allure.feature('Booking Feature')
@allure.suite('Partial Update Booking Suite')
@allure.title('Test Booking Partial Update')
@allure.description('Test to partially update a booking and verify that the response contains the updated details.')
@allure.severity(allure.severity_level.NORMAL)
def test_booking_partial_update():
    data = {
        "firstname": "James",
        "lastname": "Brown"
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': f'token={test_1_booking_token.my_token}'
    }

    with allure.step('Send PATCH request to partially update the booking'):
        response = requests.patch(
            f'https://restful-booker.herokuapp.com/booking/{test_2_booking_post.my_bookingid}',
            json=data,
            headers=headers
        )

    with allure.step('Verify the response status code is 200'):
        assert response.status_code == 200, f'Expected status code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify the updated firstname'):
        assert 'firstname' in response_data, 'Response data should contain the field "firstname".'
        assert response_data['firstname'] == data['firstname'], f"Expected firstname '{data['firstname']}', but got '{response_data['firstname']}'."

    with allure.step('Verify the updated lastname'):
        assert 'lastname' in response_data, 'Response data should contain the field "lastname".'
        assert response_data['lastname'] == data['lastname'], f"Expected lastname '{data['lastname']}', but got '{response_data['lastname']}'."

    with allure.step('Verify the response contains totalprice'):
        assert 'totalprice' in response_data, 'Response data should contain the field "totalprice".'

    with allure.step('Verify the response contains depositpaid'):
        assert 'depositpaid' in response_data, 'Response data should contain the field "depositpaid".'

    with allure.step('Verify the response contains bookingdates'):
        assert 'bookingdates' in response_data, 'Response data should contain the field "bookingdates".'

    with allure.step('Verify the bookingdates contains checkin'):
        assert 'checkin' in response_data[
            'bookingdates'], 'Response data bookingdates should contain the field "checkin".'

    with allure.step('Verify the bookingdates contains checkout'):
        assert 'checkout' in response_data[
            'bookingdates'], 'Response data bookingdates should contain the field "checkout".'

    with allure.step('Verify the response contains additionalneeds'):
        assert 'additionalneeds' in response_data, 'Response data should contain the field "additionalneeds".'


@allure.feature('Booking Feature')
@allure.suite('Partial Update Booking Suite')
@allure.title('Test Negative Partial Update Booking with Invalid Token')
@allure.description('Test to verify response when partially updating a booking with an invalid token.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_negative_partial_update_booking():
    body = {
        "firstname": "James",
        "lastname": "Brown"
    }
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Cookie': 'token=12312312'}

    with allure.step('Send PATCH request with invalid token to partially update a booking'):
        response = requests.patch(
            f'https://restful-booker.herokuapp.com/booking/{test_2_booking_post.my_bookingid}',
            json=body,
            headers=headers
        )

    with allure.step('Verify response status code is 403'):
        assert response.status_code == 403, f'Expected status code 403 but got {response.status_code}'


@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('Partial Update Booking Suite')
@allure.title('Test Negative Partial Update Booking without Token')
@allure.description('Test to verify response when partially updating a booking without a token.')
@allure.severity(allure.severity_level.CRITICAL)
def test_negative_partial_update_without_token_booking():
    body = {
        "firstname": "James",
        "lastname": "Brown"
    }
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    with allure.step('Send PATCH request without token to partially update a booking'):
        response = requests.patch(
            f'https://restful-booker.herokuapp.com/booking/{test_2_booking_post.my_bookingid}',
            json=body,
            headers=headers
        )

    with allure.step('Verify response status code is 403'):
        assert response.status_code == 403, f"Expected status code 403 but got {response.status_code}"