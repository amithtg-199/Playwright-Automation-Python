from pages.registration_page import RegistrationPage
from pages.home_page import HomePage
from utility.random_data_generator import RandomDataUtil
from playwright.sync_api import expect
import logging
import pytest

log = logging.getLogger(__name__)

faker = RandomDataUtil()

'''User Data generated from faker package'''
user_data = {
    "firstName": faker.get_first_name(),
    "lastName": faker.get_last_name(),
    "email": faker.get_email(),
    "telephone": faker.get_phone_number(),
    "password": f"{faker.get_random_alphanumeric(3)}{faker.get_password()}"
}

@pytest.mark.sanity
@pytest.mark.regression
def test_register_a_customer(page):
    '''
    Test to check the registration of random generated customer information
    '''
    try:
        register_user = RegistrationPage(page)
        home_page = HomePage(page)

        home_page.click_my_account()
        home_page.click_register()

        expect(page).to_have_title("Register Account")

        register_user.register_user(user_data=user_data)
        success_message = register_user.success_message()
        expect(success_message).to_be_visible(timeout=2000)

        my_account = register_user.continue_to_my_account()

        expect(my_account.message_heading).to_be_visible(timeout=2000)
    except Exception as e:
        log.exception(f"Test case failed with an exception {e}")

@pytest.mark.sanity
def test_register_a_customer_with_existing_email_id(page):
    '''
    Test to check if registered user_id/email_id re-registration throws Valid exception
    '''
    try:
        register_user = RegistrationPage(page)
        home_page = HomePage(page)

        home_page.click_my_account()
        home_page.click_register()

        expect(page).to_have_title("Register Account")

        register_user.register_user(user_data=user_data)

        error_message = register_user.error_when_exist_email_used()
        expect(error_message).to_be_visible(timeout=2000)
    except Exception as e:
        log.exception(f"Test case failed with an exception {e}")

@pytest.mark.sanity
@pytest.mark.regression
def test_login_registerd_account(page):
    '''
    Test to check if registered user_id/email_id is able to login sccessfully
    '''
    try:
        register_user = RegistrationPage(page)
        home_page = HomePage(page)

        home_page.click_my_account()
        home_page.click_register()

        expect(page).to_have_title("Register Account")

        login_page = register_user.click_reg_login_link()

        my_account_page = login_page.login_with_credentails(email=user_data["email"], password=user_data["password"])

        expect(my_account_page.get_acct_msg_heading()).to_be_visible(timeout=2000)
    except Exception as e:
        log.exception(f"Test case failed with an exception {e}")