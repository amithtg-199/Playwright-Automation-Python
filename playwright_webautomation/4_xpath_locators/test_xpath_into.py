import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="session")
def base_url():
    yield "https://demowebshop.tricentis.com"

def test_absolute_xpath_logo(page:Page):
    page.goto("/")
    logo = page.locator("//html/body/div[4]/div[1]/div[1]/div[1]/a/img")
    expect(logo).to_be_visible()

def test_relative_xpath_logo(page:Page):
    page.goto("/")
    logo=page.locator("//img[@alt='Tricentis Demo Web Shop']")
    expect(logo).to_be_visible()