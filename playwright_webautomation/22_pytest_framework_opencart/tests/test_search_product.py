from pages.home_page import HomePage
from playwright.sync_api import expect
import pytest
from config.config import Config

PRODUCT = Config.product_name

@pytest.mark.sanity
def test_change_currency(page):
    home_page = HomePage(page)

    currencies = [
            (home_page.select_dollar(), "$"),
            (home_page.select_euro(), "€"),
            (home_page.select_pound(), "£"),
        ]
    for currency, expected_symbol in currencies:
        home_page.currency.click()
        currency.click()
        expect(home_page.check_cart_currency()).to_contain_text(expected_symbol, timeout=2000)


def test_search_product(page):
    home_page = HomePage(page)

    home_page.enter_product_name(PRODUCT)
    search_result = home_page.click_search_products()

    msg_header = search_result.get_search_page_header()

    expect(msg_header).to_contain_text(PRODUCT, timeout=2000)

def test_is_logo_visible(page):
    home_page = HomePage(page)
    expect(home_page.logo).to_be_visible()

    

    
