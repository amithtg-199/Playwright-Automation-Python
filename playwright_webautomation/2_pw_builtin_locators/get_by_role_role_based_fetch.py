# This built-in locator os PW is used to assert a web element based on its role.

from playwright.sync_api import Page, expect

def test_get_by_text(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    expect(page.get_by_role(role='heading', name="Welcome to our store")).to_be_visible()