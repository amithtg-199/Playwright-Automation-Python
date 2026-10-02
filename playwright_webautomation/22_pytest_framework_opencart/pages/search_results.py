from playwright.sync_api import Page
from pages.product import ProductPage

class SearchItem:
    def __init__(self, page:Page):
        self.page = page
        self.search_msg_header = page.locator("#content h1", has_text="Search -")
        self.search_products = page.locator("h4 > a")

    #To check if we landed in correct product page
    def get_search_page_header(self):
        return self.search_msg_header

    #To check if product exists and valid items are retruned 
    def is_product_available(self, product_name:str):
        try:
            count = self.search_products.count()
            for i in range(count):
                product = self.search_products.nth(i)
                title = product.text_content()
                if title and title.strip() == product_name:
                    return product
        except Exception as e:
            print(f"Prdocut: {product_name} does not exists, retruned error, {e}")

    #Selection of product
    def select_product(self, product_name:str):
        try:
            product = self.is_product_available(product_name=product_name) 
            if product:
                product.click()
                return ProductPage(self.page)
        except Exception as e:
            print(f"Product: {product_name} does not exists retruned exception {e}")

    #Used to assert the count of products returned or their price
    def retrun_product_fetched(self):
        return self.search_products
