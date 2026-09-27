from playwright.sync_api import Playwright, expect
import pytest
import openpyxl
from pathlib import Path

xls_path = Path(__file__).resolve().parent
xls_file = xls_path / "data" / "data.xlsx"

workbook = openpyxl.load_workbook(xls_file)
data = workbook.active

login_data = []

for row in data.iter_rows(min_row=2, values_only=True):
    email, password, validation = row
    login_data.append((str(email or ""), str(password or ""), str(validation or "")))

workbook.close()

@pytest.mark.parametrize("email, password, validation", login_data)
def test_dd_csv_file(playwright: Playwright, email, password, validation):
    browser = playwright.chromium.launch()
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