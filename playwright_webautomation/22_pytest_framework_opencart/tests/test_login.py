from pages.login_page import LoginPage
from config.config import Config
from playwright.sync_api import expect
from pages.home_page import HomePage
from pathlib import Path
from utility.load_test_data import get_test_data_csv
import logging
import pytest

invalid_email = Config.invalid_email
invalid_password = Config.invalid_password

TEST_DATA_PATH = Path(__file__).resolve().parent.parent/"testdata"
CSV_FILE = TEST_DATA_PATH / "logindata.csv"

test_data = get_test_data_csv(CSV_FILE)

log = logging.getLogger(__name__)

@pytest.mark.smoke
def test_valid_login(page, logged_in_page):
    try:
        login_page = LoginPage(page)

        my_account = logged_in_page

        expect(my_account.get_acct_msg_heading()).to_be_visible()
    except Exception and KeyboardInterrupt as e:
        log.exception(f"Test failed with exception: {e}")

@pytest.mark.smoke
def test_invalid_login(page):
    try:
        login_page = LoginPage(page)
        home_page = HomePage(page)

        home_page.click_my_account()
        home_page.click_login()

        login_page.login_with_credentails(email=invalid_email,password=invalid_password)

        error_message = login_page.get_login_error_message()

        expect(error_message).to_be_visible(timeout=1000)
    except Exception and KeyboardInterrupt as e:
        log.exception(f"Test failed with exception: {e}")

@pytest.mark.parametrize("testName,email,password,expected", test_data)
@pytest.mark.sanity
@pytest.mark.regression
def test_login_data_driven_csv(page,testName,email,password,expected):
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.click_my_account()
    home_page.click_login()

    if expected == "success":
        log.info(f"Starting test for :{testName}")
        my_account = login_page.login_with_credentails(email=email, password=password)
        expect(my_account.get_acct_msg_heading()).to_be_visible(timeout=2000)
    elif expected == "attempt_failure":
        log.info(f"Starting test for :{testName}")
        login_page.login_with_credentails(email=email, password=password)
        expect(login_page.get_login_error_message()).to_be_visible(timeout=2000)
    else:
        log.info(f"Starting test for :{testName}")
        login_page.login_with_credentails(email=email, password=password)
        expect(login_page.get_login_error_message()).to_be_visible(timeout=2000)

    