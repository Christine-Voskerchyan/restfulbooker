import requests
import pytest
import allure
import test_2_booking_post


@pytest.mark.regression
@pytest.mark.smoke
@allure.feature('Booking Feature')
@allure.suite('Get Booking Suite')
@allure.title('Test Get All Bookings')
@allure.description('Test to retrieve all bookings and verify that the response contains at least one booking.')
@allure.severity(allure.severity_level.NORMAL)
def test_booking_get_all():
    with allure.step('Send GET request to retrieve all bookings'):
        response = requests.get('https://restful-booker.herokuapp.com/booking')

    with allure.step('Verify the response status code is 200'):
        assert response.status_code == 200, f'Expected status code 200 but got {response.status_code}'

    with allure.step('Verify the response contains at least one booking'):
        assert len(response.json()) > 0, 'Expected at least one booking but got an empty list'


@pytest.mark.regression
@pytest.mark.smoke
@allure.feature('Booking Feature')
@allure.suite('Get Booking Suite')
@allure.title('Test Get Booking By ID')
@allure.description('Test to retrieve a booking by its ID and verify the response contains correct booking details.')
@allure.severity(allure.severity_level.CRITICAL)
def test_booking_get_by_id():
    with allure.step('Send GET request to retrieve booking with ID'):
        response = requests.get(f'https://restful-booker.herokuapp.com/booking/{test_2_booking_post.my_bookingid}')

    with allure.step('Verify the response status code is 200'):
        assert response.status_code == 200, f'Expected status code 200 but got {response.status_code}'

    response_data = response.json()

    with allure.step('Check if response contains firstname'):
        assert 'firstname' in response_data, 'Response JSON does not contain firstname'

    with allure.step('Check if response contains lastname'):
        assert 'lastname' in response_data, 'Response JSON does not contain lastname'

    with allure.step('Check if response contains totalprice'):
        assert 'totalprice' in response_data, 'Response JSON does not contain totalprice'

    with allure.step('Check if response contains depositpaid'):
        assert 'depositpaid' in response_data, 'Response JSON does not contain depositpaid'

    with allure.step('Check if response contains bookingdates'):
        assert 'bookingdates' in response_data, 'Response JSON does not contain bookingdates'

    with allure.step('Check if bookingdates contains checkin'):
        assert 'checkin' in response_data['bookingdates'], 'Booking dates do not contain checkin'

    with allure.step('Check if bookingdates contains checkout'):
        assert 'checkout' in response_data['bookingdates'], 'Booking dates do not contain checkout'

    with allure.step('Check if response contains additionalneeds'):
        assert 'additionalneeds' in response_data, 'Response JSON does not contain additionalneeds'

