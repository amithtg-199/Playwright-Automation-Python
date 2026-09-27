from playwright.sync_api import Page, expect
from pathlib import Path

WD = Path(__file__).resolve().parent.parent.parent.parent
fil1_path = WD / "uploads" / "text1.txt"
file2_path = WD / "uploads" / "text.csv"

def test_upload_single_file(page:Page):
    page.goto("https://davidwalsh.name/demo/multiple-file-upload.php")

    page.locator("#filesToUpload").set_input_files(fil1_path)

    expect(page.locator("#fileList")).to_contain_text("text1.txt")

def test_multiple_files_upload(page:Page):
    page.goto("https://davidwalsh.name/demo/multiple-file-upload.php")

    list_of_files = [fil1_path, file2_path]

    page.locator("#filesToUpload").set_input_files(files=list_of_files)

    expect(page.locator("#fileList>li:nth-child(1)")).to_contain_text("text1.txt")
    expect(page.locator("#fileList>li:nth-child(2)")).to_contain_text("text.csv")
