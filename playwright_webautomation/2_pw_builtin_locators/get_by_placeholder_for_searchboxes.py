# This built-in locator os PW is used to assert a search box element with a placeholder written inside it.

from playwright.sync_api import Page, expect

def test_get_by_text(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    page.get_by_placeholder("Enter your full name").fill("item")