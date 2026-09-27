from playwright.sync_api import Page, expect

def test_drag_drop(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.get_by_role("button", name="Copy Text").dblclick()

    expect(page.locator("#field2")).to_have_value("Hello World!")