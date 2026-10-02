from playwright.sync_api import Page
from pages.shoping_cart_page import ShoppingCartPage

class ProductPage:
    def __init__(self, page:Page):
        self.page = page
        self.quantity_txt_box = page.get_by_role("textbox", name="Qty")
        self.add_to_cart_btn = page.locator("button:has-text('Add to Cart')")
        self.confirm_msg = page.locator("div.alert.alert-success.alert-dismissible")
        self.items_btn = page.locator("div#cart")
        self.view_cart_btn = page.get_by_text("View Cart", exact=True)
        self.item_in_cart = page.locator(".table.table-striped>tbody>tr")
        self.product_price = page.locator(".list-unstyled h2")

    def remove_all_product_from_cart(self):
        self.items_btn.click()
        items_count = self.item_in_cart.count()
        while items_count > 0:
            self.item_in_cart.first.locator(".btn.btn.btn-danger.btn-xs").click()

    def set_quantity(self, qty:str):
        self.quantity_txt_box.fill('')
        self.quantity_txt_box.fill(qty)

    def add_to_cart(self):
        self.add_to_cart_btn.click()

    def get_confirm_msg(self):
        return self.confirm_msg

    def click_on_items_button(self):
        self.items_btn.click()

    def click_on_view_cart(self) -> ShoppingCartPage:
        self.view_cart_btn.click()
        return ShoppingCartPage(self.page)

    #Combined Add Cart Action
    def add_product_to_cart(self, quantity:str):
        #Remove any existing product in cart
        self.remove_all_product_from_cart()
        #Set QTY
        self.set_quantity(quantity)
        #Click on Add To cart
        self.add_to_cart()
        return self.get_confirm_msg()

    def get_product_price(self):
        return self.product_price