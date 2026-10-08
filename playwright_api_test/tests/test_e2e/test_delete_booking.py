import pytest
from utils.load_data import get_payload_data
from payload_builder.payload_builder import build_payload

@pytest.mark.e2e
def test_delete_booking(request_context, generate_token):
    template = get_payload_data(payload_file="create_booking.json")
    payload, test_data = build_payload(template=template)
    response = request_context.post(url="/booking", data=payload)

    data = response.json()
    booking_id = data["bookingid"]
    print("[TEST] Booking ID is Genrated: ", booking_id)

    delete_headers = {"Content-Type":"application/json", "Cookie":f"token={generate_token}"}
    print("[TEST] Token generated:", generate_token[:5] + "**********")
    delete_response = request_context.delete(url=f"/booking/{booking_id}", headers=delete_headers)

    print("[TEST] Delete status:", delete_response.status)
    assert delete_response.status == 201, (f"Booking deletion failed: "f"{delete_response.status} - {delete_response.text()}")

