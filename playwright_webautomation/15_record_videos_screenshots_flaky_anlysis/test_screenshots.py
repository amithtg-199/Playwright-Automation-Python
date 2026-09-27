from playwright.sync_api import Playwright
from datetime import datetime
import os

def test_screenshots_page(playwright:Playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()

    os.makedirs("screenshots", exist_ok=True)
    timestamp = datetime.now().strftime(r"%d/%m/%Y%H%M%S")

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.wait_for_load_state("load")
    page.wait_for_timeout(5000)

    #partial Page_screenshot
    page.screenshot(path=f"screenshots/partial_capture_{timestamp}.png")

    #Full page screenshot
    page.screenshot(path=f"screenshots/full_capture_{timestamp}.png", full_page=True)

    #Capture an element, here we need to fetch the locator and then call the screenshot function on the locator.
    logo = page.get_by_role("img", name="client brand banner")
    logo.screenshot(path=f"screenshots/logo_{timestamp}.png")

    #Capture particular section of a page.
    quick_launch = page.locator("body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)")
    quick_launch.screenshot(path=f"screenshots/quick_launch_{timestamp}.png")

    context.close()
    browser.close()