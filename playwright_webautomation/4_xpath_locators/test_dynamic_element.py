from playwright.sync_api import Page, expect


def test_dynamic_button_start_stop(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")

    for i in range(5):
        page.locator("//button[@name='start' or @name='stop']").click()

