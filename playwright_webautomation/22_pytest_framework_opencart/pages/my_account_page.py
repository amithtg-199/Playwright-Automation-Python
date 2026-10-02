from playwright.sync_api import Page
from pages.logout_page import LogoutPage

class MyAccountPage:

    def __init__(self, page:Page):
        self.page = page
        self.message_heading = page.locator("h2:has-text('My Account')")
        self.logout_link = page.locator("div.list-group").locator("a").nth(12)

    def get_acct_msg_heading(self):
        return self.message_heading

    def click_on_logout(self):
        self.logout_link.click()
        return LogoutPage(self.page)
        