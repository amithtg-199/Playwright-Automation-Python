from playwright.sync_api import Playwright, expect


def test_bw_context(playwright:Playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page1 = context.new_page()
    page2 = context.new_page()

    page1.goto("https://playwright.dev/")
    expect(page1).to_have_title("Playwright")

    page2.goto("https://google.com")