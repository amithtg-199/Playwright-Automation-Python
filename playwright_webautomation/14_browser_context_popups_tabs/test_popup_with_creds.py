from playwright.sync_api import Playwright, expect

def test_auth_popup(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(http_credentials={"username":"admin", "password":"admin"})
    page = context.new_page()

    page.goto("https://the-internet.herokuapp.com/basic_auth")
    expect(page.locator("p")).to_be_visible()

    page.close()
    context.close()
    browser.close()