from playwright.sync_api import Page
from pages.my_account_page import MyAccountPage

class LoginPage:

    def __init__(self, page:Page):
        self.page = page
        self.email_textbox = page.get_by_role("textbox", name="E-Mail Address")
        self.password_textbox = page.get_by_label("Password")
        self.login_button = page.locator("input.btn.btn-primary")
        self.error_message = page.locator("div.alert.alert-danger.alert-dismissible")
        

    def set_email(self, email:str):
        return self.email_textbox.fill(email)

    def set_password(self, password:str):
        return self.password_textbox.fill(password)

    def login_with_credentails(self, email:str, password:str):
        self.set_email(email=email)
        self.set_password(password=password)
        self.login_button.click()
        return MyAccountPage(self.page)

    def get_login_error_message(self):
        return self.error_message