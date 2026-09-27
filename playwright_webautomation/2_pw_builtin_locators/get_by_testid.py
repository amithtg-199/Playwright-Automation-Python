# This built-in locator os PW is used to assert a web element based on test-id attribute.

from playwright.sync_api import Page, expect

def test_get_by_text(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")

    expect(page.get_by_test_id("profile-name")).to_have_text("John Doe")
    expect(page.get_by_test_id("profile-email")).to_have_text("john.doe@example.com")