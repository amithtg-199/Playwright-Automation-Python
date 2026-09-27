from playwright.sync_api import Page, expect
from pathlib import Path

CWD = Path(__file__).resolve().parent.parent.parent
file_path1 = CWD / "uploads" / "test.pdf"
file_path2 = CWD / "uploads" / "text.csv"

def test_keyboard_actions(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #set_input_files() is used to upload the file to the locator element.
    files_to_upload = [file_path1, file_path2]
    page.locator("#multipleFilesInput").set_input_files(files_to_upload)

    page.get_by_role("button", name="Upload Multiple Files").click()

    response = page.locator("#multipleFilesStatus")

    expect(response).to_contain_text("test.pdf")
    expect(response).to_contain_text("text.csv")

    