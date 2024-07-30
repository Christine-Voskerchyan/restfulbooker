import requests
import pytest
import allure
import test_1_booking_token
import test_2_booking_post


@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('Update Booking Suite')
@allure.title('Test Booking Update')
@allure.description('Test to update a booking and verify that the response contains the updated details.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.skip
def test_booking_update():
    data = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': f'token={test_1_booking_token.my_token}'
    }

    with allure.step('Send PUT request to update the booking'):
        response = requests.put(
            f'https://restful-booker.herokuapp.com/booking/{test_2_booking_post.my_bookingid}',
            json=data,
            headers=headers
        )

    with allure.step('Verify the response status code is 200'):
        assert response.status_code == 200, f'Expected 200, but got {response.status_code}. Response: {response.text}'

    response_data = response.json()

    with allure.step('Verify the updated firstname'):
        assert response_data['firstname'] == data['firstname'], f"Expected firstname '{data['firstname']}', but got '{response_data['firstname']}'"

    with allure.step('Verify the updated lastname'):
        assert response_data['lastname'] == data['lastname'], f"Expected lastname '{data['lastname']}', but got '{response_data['lastname']}'"

    with allure.step('Verify the updated totalprice'):
        assert response_data['totalprice'] == data['totalprice'], f"Expected totalprice '{data['totalprice']}', but got '{response_data['totalprice']}'"

    with allure.step('Verify the updated depositpaid'):
        assert response_data['depositpaid'] == data['depositpaid'], f"Expected depositpaid '{data['depositpaid']}', but got '{response_data['depositpaid']}'"

    with allure.step('Verify the updated bookingdates'):
        assert response_data['bookingdates'] == data['bookingdates'], f"Expected bookingdates '{data['bookingdates']}', but got '{response_data['bookingdates']}'"

    with allure.step('Verify the updated checkin date'):
        assert response_data['bookingdates']['checkin'] == data['bookingdates'][
            'checkin'], f"Expected checkin '{data['bookingdates']['checkin']}', but got '{response_data['bookingdates']['checkin']}'"

    with allure.step('Verify the updated checkout date'):
        assert response_data['bookingdates']['checkout'] == data['bookingdates']['checkout'], f"Expected checkout '{data['bookingdates']['checkout']}', but got '{response_data['bookingdates']['checkout']}'"

    with allure.step('Verify the updated additionalneeds'):
        assert response_data['additionalneeds'] == data['additionalneeds'], f"Expected additionalneeds '{data['additionalneeds']}', but got '{response_data['additionalneeds']}'"

@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('Update Booking Suite')
@allure.title('Test Negative Update Booking')
@allure.description('Test to verify response when updating a booking with an invalid token.')
@allure.severity(allure.severity_level.CRITICAL)
def test_negative_update_booking(x):
    body = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': 'token=1231786qweiy'
    }

    with allure.step('Send PUT request with invalid token to update a booking'):
        response = requests.put(
            f'https://restful-booker.herokuapp.com/booking/{test_2_booking_post.my_bookingid}',
            json=body,
            headers=headers
        )

    with allure.step('Verify response status code is 403'):
        assert response.status_code == 403, f'Expected Status Code 403, but got {response.status_code}'