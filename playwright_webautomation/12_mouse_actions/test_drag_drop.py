from playwright.sync_api import Page, expect

def test_drag_drop(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # l_source = page.locator("")
    # l_traget = page.locator("")

    page.drag_and_drop(source="#draggable", target="#droppable")
