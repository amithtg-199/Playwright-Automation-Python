from playwright.sync_api import Playwright
from payload_builder.payload_builder import build_payload
from utils.load_data import get_payload_data
from pathlib import Path
from dotenv import load_dotenv
import os
import pytest

BASE_URL = "https://restful-booker.herokuapp.com"
config_path = Path(__file__).resolve().parent/"config"
env_file = config_path/".env"

load_dotenv(dotenv_path=env_file)

@pytest.fixture(scope="session")
def request_context(playwright:Playwright):
    request =  playwright.request.new_context(base_url=BASE_URL)
    yield request
    request.dispose()

@pytest.fixture(scope="session")
def generate_token(request_context):
    headers={"Content-Type": "application/json"}

    payload={"username":os.getenv("USER_NAME"), "password":os.getenv("PASSWORD")}
    response = request_context.post(url="/auth", headers=headers, data=payload)

    assert response.ok, (f"Authentication failed: " f"{response.status} - {response.text()}")

    token = response.json()["token"]
    print("Token Geneated:", token)

    return token

@pytest.fixture(scope="session")
def create_booking(request_context, generate_token):
    '''Yields response and request payload used for test for assertion'''
    template = get_payload_data(payload_file="create_booking.json")
    payload, test_data = build_payload(template=template)
    response = request_context.post(url="/booking", data=payload)

    data = response.json()
    booking_id = data["bookingid"]
    print("[fixture-setup] Booking ID is Genrated: ", booking_id)
    
    yield response, test_data

    delete_headers = {"Content-Type":"application/json", "Cookie":f"token={generate_token}"}
    print("[fixture-teardown] Token generated:", generate_token[:5] + "**********")
    delete_response = request_context.delete(url=f"/booking/{booking_id}", headers=delete_headers)

    print("[fixture-teardown] Delete status:", delete_response.status)
    assert delete_response.status == 201, (f"Booking deletion failed: "f"{delete_response.status} - {delete_response.text()}")