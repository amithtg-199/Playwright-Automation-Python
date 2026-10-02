from playwright.sync_api import Page
from pages.search_results import SearchItem

class HomePage:
    def __init__(self, page:Page):
        self.page = page
        self.myacct_link = page.locator("span:has-text('My Account')")
        self.register_link = page.get_by_role("link", name="Register")
        self.login_link = page.get_by_role("link", name="Login")
        self.searchbox = page.get_by_role("textbox", name="Search")
        self.search_button = page.locator("button.btn.btn-default.btn-lg")    
        self.currency = page.get_by_text("Currency", exact=True)
        self.euro = page.get_by_role("button", name="€ Euro")
        self.dollar = page.get_by_role("button", name="$ US Dollar")
        self.pound = page.get_by_role("button", name="£ Pound Sterling")
        self.cart_currency = page.locator("button span#cart-total")
        self.logo = page.get_by_role("img", name="naveenopencart")

    def get_home_page_title(self):
        title = self.page.title()
        return title
    
    def click_my_account(self):
        self.myacct_link.click()

    def click_register(self):
        self.register_link.click()

    def click_login(self):
        self.login_link.click()

    def click_currency(self):
        self.currency.click()

    def select_dollar(self):
        return self.dollar

    def select_euro(self):
        return self.euro

    def select_pound(self):
        return self.pound
    #This retruns the Cart curreny locator which will have text where the curreny will be mentioned
    #can be used for assertion after changing the currency.
    def check_cart_currency(self):
        return self.cart_currency

    def enter_product_name(self, product_name):
        self.searchbox.fill(product_name)

    def click_search_products(self):
        self.search_button.click()
        return SearchItem(self.page)

    def get_logo(self):
        return self.logo

    