from playwright.sync_api import Playwright, expect
import pytest


@pytest.mark.parametrize("items", ["computer", "laptop", "jeans", "monitor"])

def test_dd_select_products(playwright:Playwright, items):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://demowebshop.tricentis.com/")

    page.locator("#small-searchterms").fill(items)
    page.locator("input.button-1.search-box-button").click()
    try:
        expect(page.locator("h2[class$='product-title']").nth(0)).to_contain_text(items, ignore_case=True)
    except Exception as e:
        pytest.fail(f"Received an error {e}")
    finally:
        context.close()
        browser.close()