from playwright.sync_api import Page, expect
from pathlib import Path

CWD = Path(__file__).resolve().parent.parent.parent
file_path = CWD / "uploads" / "text1.txt"

def test_keyboard_actions(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #set_input_files() is used to upload the file to the locator element.
    page.locator("#singleFileInput").set_input_files(file_path)

    page.get_by_role("button", name="Upload Single File").click()

    expect(page.locator("#singleFileStatus")).to_contain_text("text1.txt")
    