from playwright.sync_api import Page, expect

def test_keyboard_actions(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #Focus on input box 1
    input1 = page.locator("#input1")
    input1.focus()

    page.keyboard.insert_text("Welcome")
    page.keyboard.press("Control+A")
    page.keyboard.press("Control+C")

    input2 = page.locator("#input2")
    input2.focus()

    page.keyboard.press("Control+V")

    input3 = page.locator("#input3")
    input3.focus()

    page.keyboard.press("Control+V")

    expect(input1).to_have_value("Welcome")
    expect(input2).to_have_value("Welcome")
    expect(input3).to_have_value("Welcome")
