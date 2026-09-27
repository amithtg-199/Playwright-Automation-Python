from playwright.sync_api import Playwright, expect

def test_tab_pages(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://testautomationpractice.blogspot.com/")

    with context.expect_page() as page_info:
        page.locator("button[onclick='myFunction()']").click()

    tabs = page_info.value

    tabs.wait_for_load_state()

    all_pages = context.pages

    print("Number of Pages: ", len(all_pages))

    print("Parent_page: ", all_pages[0].url)

    print("Second_page: ", all_pages[1].url)