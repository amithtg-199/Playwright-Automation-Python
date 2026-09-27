import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="session")
def base_url():
    yield "https://demowebshop.tricentis.com"

def test_absolute_xpath_logo(page:Page):
    page.goto("/")
    #Here if we need to use a relative Xpath then we use // and a attribute is identified by @attribute
    computer_products = page.locator("//h2//a[contains(@href,'computer')]")
    computer_products_count = computer_products.count() #Here count method counts from 1
    expect(computer_products).to_have_count(computer_products_count)

def test_fetch_first_last_nth_element(page:Page):
    page.goto("/")
    computer_products = page.locator("//h2//a[contains(@href,'computer')]")
    print("First Element: ", computer_products.first.text_content()) #Fetches first element
    print("Last Element: ", computer_products.last.text_content()) #Fetches first element
    print("nth Element: ", computer_products.nth(2).text_content()) #Fetches first element

def test_count_startswith_build(page:Page):
    page.goto("/")
    building_product = page.locator("//h2//a[starts-with(@href,'/build')]")
    print("Building product total count: ", building_product.count())
    expect(building_product).to_have_count(building_product.count())

def test_inner_text_fetch(page:Page):
    page.goto("/")
    expect(page.locator("//a[text()='Register']")).to_have_text("Register", ignore_case=True)

def test_fetch_last_element_xpath(page:Page):
    page.goto("/")
    expect(page.locator("//div[@class='column follow-us']//li[last()]")).to_have_text("Google+")