from playwright.sync_api import Page
import os
import pytest

def test_keyboard_actions(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")

    page.get_by_role("textbox", name="Enter Text:").fill("Welcome")
    page.get_by_role("button", name="Generate and Download Text File").click()

    ''' If we use the below ones then it brings up Race condition in PW while execution, i.e. after below two commnands are executed 
    Py will not wait for file download it immediately rushes to check if file exists or not.
    # page.on("download", lambda download: download.save_as("download/testdownload.txt"))
    # page.locator("#txtDownloadLink").click()
    '''

    with page.expect_download() as download_info:
        page.locator("#txtDownloadLink").click()

    download = download_info.value

    os.makedirs("download", exist_ok=True)

    download.save_as("download/test_text_download.txt")
    
    if os.path.exists("download/test_text_download.txt"):
        print("File exists")
    else:
        pytest.fail("File does not exists")
