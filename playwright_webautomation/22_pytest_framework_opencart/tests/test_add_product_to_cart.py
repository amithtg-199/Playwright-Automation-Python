from pages.home_page import HomePage
from pages.search_results import SearchItem
from playwright.sync_api import expect
from config.config import Config
import logging
import pytest

log = logging.getLogger(__name__)

PRODUCT = Config.product_name
PRODUCT_QTY = Config.product_quantity
PRODUCT_PRICE = Config.total_price

@pytest.mark.sanity
def test_selected_product_exists(page):
    home_page = HomePage(page)

    home_page.enter_product_name(PRODUCT)
    search_result_page = home_page.click_search_products()

    msg_header = search_result_page.get_search_page_header()
    expect(msg_header).to_be_visible(timeout=2000)

    product = search_result_page.is_product_available(PRODUCT)
    product_name = product.inner_text()
    log.info(f"Product {product_name} exists")

    expect(product).to_contain_text(PRODUCT)

@pytest.mark.sanity
def test_price_of_selected_product(page):
    home_page = HomePage(page)

    home_page.enter_product_name(PRODUCT)
    search_result_page = home_page.click_search_products()

    product_page = search_result_page.select_product(PRODUCT)

    price = product_page.get_product_price()
    price_value = price.inner_text()
    log.info(f"Product {PRODUCT} price is: {price_value}")

    expect(price).to_have_text(PRODUCT_PRICE)

@pytest.mark.sanity
@pytest.mark.regression
def test_add_product_to_cart(page):
    home_page = HomePage(page)

    home_page.enter_product_name(PRODUCT)
    search_result_page = home_page.click_search_products()

    product_page = search_result_page.select_product(PRODUCT)

    confirm_msg = product_page.add_product_to_cart(PRODUCT_QTY)

    expect(confirm_msg).to_be_visible(timeout=2000)



