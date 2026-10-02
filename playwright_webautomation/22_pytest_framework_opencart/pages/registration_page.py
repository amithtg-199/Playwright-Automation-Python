from playwright.sync_api import Page
from pages.my_account_page import MyAccountPage
from pages.login_page import LoginPage

class RegistrationPage:

    def __init__(self,page:Page):
        self.page = page
        self.first_name = page.get_by_role("textbox", name="First Name")
        self.last_name = page.get_by_role("textbox", name="Last Name")
        self.email = page.get_by_role("textbox", name="E-Mail")
        self.telephone = page.get_by_role("textbox", name="Telephone")
        self.password = page.get_by_label("Password", exact=True)
        self.confirm_password = page.get_by_label("Password Confirm")
        self.newsletter_enable = page.get_by_label("Yes")
        self.policy_checkbox = page.locator("[name='agree']")
        self.continue_btn = page.locator("input.btn.btn-primary")
        self.success_msg = page.get_by_role("heading", name="Your Account Has Been Created!")
        self.error_msg_used_email = page.get_by_text("Warning: E-Mail Address is already registered!", exact=True)

        #Confirmation continue Button:
        self.confirm_to_myaccount = page.get_by_role("link", name="Continue")

        #login_link in Registration Page
        self.login_lnk = page.get_by_role("link", name="login page")


    def fill_first_name(self, first_name):
        self.first_name.fill(first_name)

    def fill_last_name(self, last_name):
        self.last_name.fill(last_name)

    def fill_email_id(self, email_id):
        self.email.fill(email_id)

    def fill_telephone_number(self, telphone_number):
        self.telephone.fill(telphone_number)

    def fill_password(self, password):
        self.password.fill(password)

    def fill_confirm_password(self, password):
        self.confirm_password.fill(password)

    def check_newsleter(self):
        return self.newsletter_enable

    def check_policy(self):
        self.policy_checkbox.check()

    def click_continue(self):
        self.continue_btn.click()

    def success_message(self):
        return self.success_msg

    #This is to check post registration if we are landing into My Account page.
    def continue_to_my_account(self):
        self.confirm_to_myaccount.click()
        return MyAccountPage(self.page)

    def error_when_exist_email_used(self):
        return self.error_msg_used_email

    def click_reg_login_link(self):
        self.login_lnk.click()
        return LoginPage(self.page)

    def register_user(self, user_data: dict):

        '''
        Complete the full registration process using provided user data.

        Example:
        user_data = {
            "firstName": "John",
            "lastName": "Doe",
            "email": "john.doe@example.com",
            "telephone": "9876543210",
            "password": "Test@123"
        }
        '''
        self.fill_first_name(user_data['firstName'])
        self.fill_last_name(user_data['lastName'])
        self.fill_email_id(user_data['email'])
        self.fill_telephone_number(user_data['telephone'])
        self.fill_password(user_data['password'])
        self.fill_confirm_password(user_data['password'])
        self.check_policy()
        self.click_continue()

        return self.success_msg
    