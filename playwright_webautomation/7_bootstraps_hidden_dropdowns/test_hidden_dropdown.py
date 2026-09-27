import pytest
from playwright.sync_api import Page, expect
from random import choice


def test_count_total_options_hidden_dropdown(login_page:Page):
    login_page.goto("/web/index.php/dashboard/index")

    login_page.get_by_text("PIM", exact=True).click()

    #Select the dropdown of Job Title
    login_page.locator(".oxd-icon.bi-caret-down-fill.oxd-select-text--arrow").nth(2).click()

    #Get all 28 options excluding "select_options"
    options_locator = login_page.locator("div[role='listbox'] span")
    # Wait for the dropdown to be visible, because all_text_contents function executes immedeatley, and does not wait.
    options_locator.first.wait_for(state="visible")

    options_count = options_locator.count()

    expect(options_locator).to_have_count(options_count)

def test_select_random_options_hidden_dropdown(login_page:Page):
    login_page.goto("/web/index.php/dashboard/index")

    login_page.get_by_text("PIM", exact=True).click()

    #Select the dropdown of Job Title
    login_page.locator(".oxd-icon.bi-caret-down-fill.oxd-select-text--arrow").nth(2).click()

    #Get all 28 options excluding "select_options"
    options_locator = login_page.locator("div[role='listbox'] span")
    # Wait for the dropdown to be visible, because all_text_contents function executes immedeatley, and does not wait.
    options_locator.first.wait_for(state="visible")

    job_titles_options = options_locator.all_text_contents()

    #Get the index of the hidden dropdown option, next is used 
    to_select = next(((idx, value) for idx,value in enumerate(job_titles_options) if value == "Financial Analyst"), None)

    #Select the option using nth function 
    options_locator.nth(to_select[0]).click()
