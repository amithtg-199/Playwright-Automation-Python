# This built-in locator os PW is used to assert if a web element text displayed on the webpage.

from playwright.sync_api import Page, expect
import re #Used for regular expression

def test_get_by_text(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    expect(page.get_by_text('Welcome to the new Tricentis store!')).to_be_visible() #Full Text
    # expect(page.get_by_text('Welcome to')).to_be_visible() # Partial text
    # expect(page.get_by_text(re.compile('.*Welcome.*'))).to_be_visible() # By using regular expression