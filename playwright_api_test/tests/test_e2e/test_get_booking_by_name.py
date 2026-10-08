import pytest
import json

@pytest.mark.e2e
def test_get_booking_id_by_f_name_l_name(create_booking, request_context):
    response, test_data = create_booking

    firstname = test_data["first_name"]
    lastname = test_data["last_name"]
    params = {"firstname":f"{firstname}","lastname":f"{lastname}"}

    bookingid_response = request_context.get(url="/booking", params=params)

    assert bookingid_response.status == 200

    data = bookingid_response.json()

    print(f"[TEST] Booking Id fetched for {firstname} {lastname} is: {json.dumps(data, indent=4)} ")

    assert len(data) > 0