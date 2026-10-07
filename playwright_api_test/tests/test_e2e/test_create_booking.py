import pytest

@pytest.mark.e2e
def test_create_booking(create_booking):
    response, test_data = create_booking

    data = response.json()
    assert response.ok, (f"Create Booking failed with: {response.status}-{response.text()}" )
    print(f"[TEST] Booking id: {data["bookingid"]} created for {test_data["first_name"]} {test_data["last_name"]}")

