# This built-in locator os PW is used to assert a web element based on title.

from playwright.sync_api import Page, expect

def test_get_by_text(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")

    expect(page.get_by_title("Home page link")).to_have_text("Home")