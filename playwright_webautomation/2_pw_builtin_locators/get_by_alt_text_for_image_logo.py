# This built-in locator os PW is used to assert if an image or Logo is properly loaded or not.

from playwright.sync_api import Page, expect

def test_get_alt_by_text(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    # Here get_by_alt_text retruns the locator so we need to store in a var and then use to assert it.
    logo = page.get_by_alt_text("Tricentis Demo Web Shop")
    # To be visile makes sure the logo is loaded sucesfully upon the browser is up.
    expect(logo).to_be_visible()