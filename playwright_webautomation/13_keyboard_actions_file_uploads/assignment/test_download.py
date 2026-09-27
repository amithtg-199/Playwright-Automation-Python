from playwright.sync_api import Page
import os
import pytest

def test_download_pdf(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")

    page.get_by_role("textbox", name="Enter Text:").fill("Welcome PDF")
    page.get_by_role("button", name="Generate and Download PDF File").click()

    with page.expect_download() as download_info:
        page.locator("#pdfDownloadLink").click()
        

    download = download_info.value
    os.makedirs("downloads", exist_ok=True)
    download.save_as("downloads/test_pdf_file.pdf")

    if os.path.exists("downloads/test_pdf_file.pdf"):
        print("File exists")
    else:
        pytest.fail("File does not exists")