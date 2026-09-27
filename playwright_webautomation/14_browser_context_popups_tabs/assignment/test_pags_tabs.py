from playwright.sync_api import Playwright, expect

def test_pages_tabs(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

# Test login
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

# Test Helper page link

    with context.expect_page() as page_info:
        page.get_by_role("link", name="OrangeHRM, Inc").click()

    l_page = page_info.value

    l_page.wait_for_load_state()

    all_pages = context.pages

    print("Number of Pages loaded: ", len(all_pages))

    all_pages[1].locator("button.nav-link.contact-btn-nav:visible").click()
    expect(all_pages[1]).to_have_url("https://orangehrm.com/contact-sales")

    context.close()
    browser.close()
    
