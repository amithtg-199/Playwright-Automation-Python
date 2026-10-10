from playwright.sync_api import Playwright, expect
from utils.load_data import get_payload_data, get_json_schema
from payload_builder.payload_builder import build_payload
from utils.json_schema_validator import json_schema_validator
import json

def test_create_booking(playwright:Playwright):

    template = get_payload_data(
        "create_booking.json"
    )

    payload, test_data = build_payload(template)

    request = playwright.request.new_context(
        base_url="https://restful-booker.herokuapp.com"
    )

    response = request.post(
        "/booking",
        data=payload
    )
    print(f"Final Request Payload ==> {payload}")
    expect(response).to_be_ok()

    response_body = response.json()
    print(f"Response received from Thrid Party ==> {json.dumps(obj=response_body, indent=4)}")

    assert response_body["booking"]["firstname"] == test_data["first_name"]

    assert response_body["booking"]["lastname"] == test_data["last_name"]

    assert response_body["booking"]["totalprice"] == test_data["total_price"]

    assert response_body["booking"]["depositpaid"] == test_data["deposit_paid"]

    request.dispose()

def test_create_booking_response_schema_validation(create_booking):
    response,test_data = create_booking

    response_body = response.json()

    schema = get_json_schema("create_booking_scheam.json")

    result = json_schema_validator(json_response=response_body,json_scehma=schema)

    assert result, ("[TEST] JSON Response Schema Validation Failed")