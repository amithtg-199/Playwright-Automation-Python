import pytest

@pytest.mark.e2e
def test_get_booking_info(create_booking, request_context):
    response, test_data = create_booking
    headers = {"Accept":"application/json"}
    booking_id = response.json()["bookingid"]
    print(f"[TEST] Booking ID for which data to fetch: {booking_id}")

    get_response = request_context.get(url=f"booking/{booking_id}", headers=headers)

    assert get_response.status == 200

    get_data = get_response.json()

    print(f"[TEST] Data returned for booking_id: {booking_id} is {get_data["firstname"]} {get_data["lastname"]}")
    assert get_data["firstname"] == test_data["first_name"]
    assert get_data["lastname"] == test_data["last_name"]
    assert get_data["bookingdates"]["checkin"] == test_data["checkin_date"]
    assert get_data["bookingdates"]["checkout"] == test_data["checkout_date"]


