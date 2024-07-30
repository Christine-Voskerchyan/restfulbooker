import requests
import pytest
import allure

my_bookingid = 0

@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('Create Booking Suite')
@allure.title('Test Create Booking')
@allure.description('Test to create a booking and verify the response.')
@allure.severity(allure.severity_level.CRITICAL)
def test_create_booking():
    data = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send POST request to create booking'):
        response = requests.post(
            'https://restful-booker.herokuapp.com/booking',
            json=data,
            headers=headers
        )

    with allure.step('Verify the response status code is 200'):
        assert response.status_code == 200, f'Expected status code 200 but got {response.status_code}'

    response_data = response.json()

    with allure.step('Check if response contains booking ID'):
        assert "bookingid" in response_data, 'Response JSON does not contain bookingid'

    with allure.step('Check if response contains booking details'):
        assert "booking" in response_data, 'Response JSON does not contain booking'

    response_booking = response_data['booking']

    with allure.step('Check if booking contains firstname'):
        assert "firstname" in response_booking, 'Booking does not contain firstname'

    with allure.step('Check if booking contains lastname'):
        assert "lastname" in response_booking, 'Booking does not contain lastname'

    with allure.step('Check if booking contains totalprice'):
        assert "totalprice" in response_booking, 'Booking does not contain totalprice'

    with allure.step('Check if booking contains depositpaid'):
        assert "depositpaid" in response_booking, 'Booking does not contain depositpaid'

    with allure.step('Check if booking contains bookingdates'):
        assert "bookingdates" in response_booking, 'Booking does not contain bookingdates'

    with allure.step('Check if bookingdates contains checkin'):
        assert "checkin" in response_booking['bookingdates'], 'Booking dates do not contain checkin'

    with allure.step('Check if bookingdates contains checkout'):
        assert "checkout" in response_booking['bookingdates'], 'Booking dates do not contain checkout'

    with allure.step('Check if booking contains additionalneeds'):
        assert "additionalneeds" in response_booking, 'Booking does not contain additionalneeds'

    with allure.step('Validate firstname in response matches input'):
        assert response_booking['firstname'] == data[
            'firstname'], f'Expected firstname {data["firstname"]} but got {response_booking["firstname"]}'

    with allure.step('Validate lastname in response matches input'):
        assert response_booking['lastname'] == data[
            'lastname'], f'Expected lastname {data["lastname"]} but got {response_booking["lastname"]}'

    with allure.step('Validate totalprice in response matches input'):
        assert response_booking['totalprice'] == data[
            'totalprice'], f'Expected totalprice {data["totalprice"]} but got {response_booking["totalprice"]}'

    with allure.step('Validate depositpaid in response matches input'):
        assert response_booking['depositpaid'] == data[
            'depositpaid'], f'Expected depositpaid {data["depositpaid"]} but got {response_booking["depositpaid"]}'

    with allure.step('Validate bookingdates in response matches input'):
        assert response_booking['bookingdates'] == data[
            'bookingdates'], f'Expected bookingdates {data["bookingdates"]} but got {response_booking["bookingdates"]}'

    with allure.step('Validate checkin date in response matches input'):
        assert response_booking['bookingdates']['checkin'] == data['bookingdates'][
            'checkin'], f'Expected checkin {data["bookingdates"]["checkin"]} but got {response_booking["bookingdates"]["checkin"]}'

    with allure.step('Validate checkout date in response matches input'):
        assert response_booking['bookingdates']['checkout'] == data['bookingdates'][
            'checkout'], f'Expected checkout {data["bookingdates"]["checkout"]} but got {response_booking["bookingdates"]["checkout"]}'

    with allure.step('Validate additionalneeds in response matches input'):
        assert response_booking['additionalneeds'] == data[
            'additionalneeds'], f'Expected additionalneeds {data["additionalneeds"]} but got {response_booking["additionalneeds"]}'

    global my_bookingid
    my_bookingid = response_data['bookingid']




