from playwright.sync_api import expect
from pages.home_page import HomePage
import pytest
import logging
from config.config import Config

log = logging.getLogger(__name__)

TOTAL_PRICE = Config.total_price
PRODUCT = Config.product_name
PRODUCT_QTY = Config.product_quantity

@pytest.mark.sanity
def test_check_price_before_checkout(page):
    home_page = HomePage(page)

    home_page.enter_product_name(PRODUCT)
    search_items_page = home_page.click_search_products()

    product_page = search_items_page.select_product(PRODUCT)

    confirm_msg = product_page.add_product_to_cart(PRODUCT_QTY)
    expect(confirm_msg).to_be_visible(timeout=2000)

    product_page.click_on_items_button()
    shoping_page = product_page.click_on_view_cart()

    total_price = shoping_page.get_total_price()
    total = total_price.inner_text()
    log.info(f"Total Price of cart is: {total}")
    expect(total_price).to_have_text(TOTAL_PRICE)

@pytest.mark.sanity
def test_check_is_product_out_ofstock(page):
    home_page = HomePage(page)

    home_page.enter_product_name(PRODUCT)
    search_items_page = home_page.click_search_products()

    product_page = search_items_page.select_product(PRODUCT)

    confirm_msg = product_page.add_product_to_cart(PRODUCT_QTY)
    expect(confirm_msg).to_be_visible(timeout=2000)

    product_page.click_on_items_button()
    shoping_page = product_page.click_on_view_cart()

    out_of_stock_msg = shoping_page.is_product_out_of_stock()
    msg_text = out_of_stock_msg.inner_text()

    log.info(f"The product {PRODUCT} is out of stock and {msg_text} is dispalyed")

    expect(out_of_stock_msg).to_be_visible()

