from playwright.sync_api import Page
#route=account/logout
class LogoutPage:

    def __init__(self,page:Page):
        self.page = page
        self.continue_button = page.get_by_role("link", name="Continue")

    def click_on_continue(self):
        self.continue_button.click()

    def get_continue_button(self):
        return self.continue_button
        