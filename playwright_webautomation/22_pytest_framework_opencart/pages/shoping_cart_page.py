from playwright.sync_api import Page

class ShoppingCartPage:

    def __init__(self, page:Page):
        self.page = page
        self.total_price = page.locator(".col-sm-4.col-sm-offset-8 tbody>tr:last-child>td:nth-child(2)")
        self.checkout_btn = page.locator("a.btn.btn-primary")
        self.out_of_stock_msg = page.locator("div.alert.alert-danger.alert-dismissible")

    def is_shopping_page_loaded(self):
        return self.checkout_btn

    def get_total_price(self):
        return self.total_price

    def is_product_out_of_stock(self):
        return self.out_of_stock_msg