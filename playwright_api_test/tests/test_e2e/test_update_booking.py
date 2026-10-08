import pytest
from payload_builder.payload_builder import build_payload
from utils.load_data import get_payload_data

@pytest.mark.e2e
def test_update_booking_info(create_booking, request_context, generate_token):
    response, test_data = create_booking
    booking_id = response.json()["bookingid"]

    token = generate_token

    template = get_payload_data("update_booking.json")
    payload,update_test_data = build_payload(template=template)

    headers = {"Content-Type":"application/json", "Accept":"application/json", "Cookie":f"token={token}"}

    update_response = request_context.put(url=f"/booking/{booking_id}", headers=headers, data=payload)

    assert update_response.ok
    assert update_response.status == 200, (f"Response failed with status code: {response.status}-{response.text()}")

    data = update_response.json()
    print(f"[TEST] Updated Booking information for {booking_id} to {data["firstname"]} {data["lastname"]} and price {data["totalprice"]}")

    assert data["firstname"] == update_test_data["first_name"]
    assert data["totalprice"] == update_test_data["total_price"]