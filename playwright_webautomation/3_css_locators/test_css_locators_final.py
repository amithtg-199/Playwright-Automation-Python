from playwright.sync_api import Page, expect
import pytest

@pytest.fixture(scope="session")
def base_url():
    yield "https://demowebshop.tricentis.com"


def test_logo_is_visible(page: Page):
    page.goto("/")
    expect(page.get_by_alt_text("Tricentis Demo Web Shop")).to_be_visible()

def test_count_of_computer_featured_product(page: Page):
    page.goto("/")
    #Checking the count of elements fetched
    expect(page.locator("h2>a[href*='computer']")).to_have_count(4)

def test_get_first_computer_featured_product(page: Page):
    page.goto("/")
    # Check the first element
    print("first computer name is: ", page.locator("h2 > a[href*='computer']").nth(0).text_content())
    expect(page.locator("h2 > a[href*='computer']").nth(0)).to_have_text("Build your own cheap computer")

def test_get_last_computer_featured_product(page: Page):
    page.goto("/")
    # Check the first element
    print("Last Computer Name is: ", page.locator("h2 > a[href*='computer']").nth(3).text_content())
    expect(page.locator("h2 > a[href*='computer']").nth(3)).to_have_text("simple Computer", ignore_case=True)

def test_get_2_computer_featured_product(page: Page):
    page.goto("/")
    # Check the first element
    print("2nd Computer Name is: ", page.locator("h2 > a[href*='computer']").nth(1).text_content())
    expect(page.locator("h2 > a[href*='computer']").nth(1)).to_have_text("Build your own computer",ignore_case=True)

def test_get_title_of_all_computer_products(page: Page):
    page.goto("/")
    print("All Products Title: ", page.locator("h2 > a[href*='computer']").all_text_contents())

def test_get_list_of_links_under_follow_us(page: Page):
    page.goto("/")
    print("First_ link : \n", page.locator(".follow-us a").nth(0).text_content())
    print("Last_ link : \n", page.locator(".follow-us a").nth(4).text_content())
    print("2nd_ link : \n", page.locator(".follow-us a").nth(1).text_content())
    