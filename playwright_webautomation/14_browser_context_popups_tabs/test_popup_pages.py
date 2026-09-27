from playwright.sync_api import Playwright, expect

def test_popup_pages(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://testautomationpractice.blogspot.com/")

    with page.expect_popup() as popup_info:
        page.locator("#PopUp").click()

    popup = popup_info.value

    popup.wait_for_load_state()

    all_pages = context.pages

    print("Total Number os pages/Popups opened: ", len(all_pages))

    for pw in all_pages:
        print("Web page URLs are ===>", pw.url)
        title = pw.title()
        if "Playwright" in title:
            pw.locator(".getStarted_Sjon").click()
            expect(pw).to_have_title("Installation | Playwright")
            pw.close()

    context.close()
    browser.close()
