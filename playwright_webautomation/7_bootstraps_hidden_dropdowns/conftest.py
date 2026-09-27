import pytest
from playwright.sync_api import Browser, Playwright, Page, APIRequestContext
import os
from typing import Generator

AUTH_FILE = "auth/auth.json"
BASE_URL = "https://opensource-demo.orangehrmlive.com/"


def is_session_valid(playwright: Playwright) -> bool:
    if not os.path.exists(AUTH_FILE):
        return False

    # If valid file exists then load the auth session to browser context
    context = playwright.request.new_context(base_url=BASE_URL,storage_state=AUTH_FILE)

        #Fire a lightweight request to check the Auth state.
    try:
        response = context.get("/web/index.php/performance/searchEvaluatePerformanceReview")
        return response.ok and "auth/login" not in response.url
    except Exception:
        return False
    finally:
        context.dispose()

def login_via_api(playwright: Playwright) -> str:
    # Make sure the path exists
    os.makedirs(os.path.dirname(AUTH_FILE), exist_ok=True)

    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(base_url=BASE_URL)
    page = context.new_page()

    try:
        page.goto("/web/index.php/auth/login")
        page.get_by_placeholder("Username").fill("Admin")
        page.get_by_placeholder("Password").fill("admin123")
        page.get_by_role("button", name="Login").click()

        page.wait_for_url("**/dashboard/index")
        context.storage_state(path=AUTH_FILE)
    except Exception as e:
        print(f"Received and Excpection: {e} while attempting to login")
    finally:
        page.close()
        context.close()
        browser.close()

    return AUTH_FILE

@pytest.fixture(scope="session")
def session_auth_state(playwright: Playwright) -> str:
    if not is_session_valid(playwright=playwright):
        if os.path.exists(AUTH_FILE):
            os.remove(AUTH_FILE)

        print("\n[Auth Engine] Session Expired, generating new Auth state")
        login_via_api(playwright)
    else:
        print("\n[Auth Engine] Valid session restored from cache.")
    return AUTH_FILE

@pytest.fixture(scope="function")
def login_page(browser: Browser, session_auth_state:str) -> Generator[Page, None, None]:
    context = browser.new_context(base_url=BASE_URL, storage_state=session_auth_state)
    page = context.new_page()

    yield page

    page.close()
    context.close()


            

    