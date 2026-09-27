from playwright.sync_api import Playwright, expect
import pytest
import json
from pathlib import Path

json_path = Path(__file__).resolve().parent
json_file = json_path / "data" / "data.json"

with open(json_file, "r") as f:
    test_data = json.load(fp=f)

@pytest.mark.parametrize("email, password, validation", [(item["email"], item["password"], item["validity"]) for item in test_data])
def test_dd_select_products(playwright:Playwright, email, password, validation):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://demowebshop.tricentis.com/login")

    page.get_by_role("textbox", name="Email:").fill(email)
    page.get_by_label("Password:").fill(password)

    page.locator("input.button-1.login-button").click()
    try:
        if validation == "valid":
            logout_button = page.get_by_role("link", name="Log out")
            expect(logout_button).to_be_visible(timeout=4000)
        else:
            error_message = page.locator("div.validation-summary-errors")
            expect(error_message).to_be_visible(timeout=3000)
            expect(page).to_have_url("https://demowebshop.tricentis.com/login")
    except Exception as e:
        pytest.fail(f"Test case failed with exception {e}")
    finally:
        context.close()
        browser.close()
