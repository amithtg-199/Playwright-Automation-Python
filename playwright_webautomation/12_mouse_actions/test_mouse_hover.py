from playwright.sync_api import Page, expect

def test_mouse_hover(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    point_me = page.get_by_role("button", name="Point Me")
    point_me.hover()

    mobile = page.locator(".dropdown-content>a:nth-child(1)")
    mobile.hover()