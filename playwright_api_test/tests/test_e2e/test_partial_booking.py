import pytest
from payload_builder.payload_builder import build_payload
from utils.load_data import get_payload_data

@pytest.mark.e2e
def test_partial_booking_update(create_booking, request_context, generate_token):
    response, test_data = create_booking
    booking_id = response.json()["bookingid"]

    token = generate_token

    template = get_payload_data("partial_booking.json")
    payload, partial_upd_test_data = build_payload(template=template)

    headers = {"Content-Type":"application/json", "Accept":"application/json", "Cookie":f"token={token}"}

    partial_upd_response = request_context.patch(url=f"/booking/{booking_id}", headers=headers, data=payload)

    assert partial_upd_response.ok
    assert partial_upd_response.status == 200

    data = partial_upd_response.json()

    print(f"[TEST] updated firstname and lastname for booking_id: {booking_id} to {data["firstname"]} {data["lastname"]}")

    assert data["firstname"] == partial_upd_test_data["first_name"]
    assert data["lastname"] == partial_upd_test_data["last_name"]