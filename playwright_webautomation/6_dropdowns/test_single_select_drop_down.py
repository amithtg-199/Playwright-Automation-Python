from playwright.sync_api import Page, expect
from random import choice

def test_single_select_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    raw_countries = page.locator("#country option").all_text_contents()
    clean_countries_list = [country.strip() for country in raw_countries]
    # print(clean_countries_list)
    country = choice(clean_countries_list)
    # print(country)
    page.locator("#country").select_option(label=country)

def test_number_of_options(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    all_options = page.locator("#country option")
    expect(all_options).to_have_count(10)
    
    



    