from playwright.sync_api import Page, expect

def test_verify_search_data(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")

    for i in range(5):
        page.locator("button[class*='start'], button[class*='stop']").click()