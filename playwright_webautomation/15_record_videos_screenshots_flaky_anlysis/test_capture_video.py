from playwright.sync_api import Playwright, expect
import os

def test_capture_vid(playwright:Playwright):

    os.makedirs("videos", exist_ok=True)

    browser = playwright.chromium.launch()

    # Send below paramter to record the test-cases
    context = browser.new_context(
        record_video_dir="videos/",
        record_video_size={"height":1024, "width":768}
    )

    page = context.new_page()

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    expect(page).to_have_title("OrangeHRM")

    context.close()
    browser.close()

    