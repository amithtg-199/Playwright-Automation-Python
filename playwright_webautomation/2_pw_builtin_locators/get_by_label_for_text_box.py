# This built-in locator os PW is used to assert a element based on label asscoaited with another element like text-box.

from playwright.sync_api import Page, expect

def test_get_by_text(page: Page):
    page.goto("https://demowebshop.tricentis.com/register")

    page.get_by_label("First name:").fill("Joe")
    page.get_by_label("Last name:").fill("Black")
    page.get_by_label("Email:").fill("abcd@gmail.com")