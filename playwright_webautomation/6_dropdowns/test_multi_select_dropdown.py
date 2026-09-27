from playwright.sync_api import Page, expect
from random import choices
import pytest

def test_multi_select_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    raw_colours = page.locator("#colors option").all_text_contents()
    clean_colours = [colour.strip() for colour in raw_colours]

    colour = choices(clean_colours, k=3)

    page.locator("#colors").select_option(label=colour)

def test_count_options_retruned_from_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    raw_colours = page.locator("#colors option")

    expect(raw_colours).to_have_count(7)

def test_colour_dropdown_not_sorted(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    raw_colours = page.locator("#colors option").all_text_contents()
    clean_colours = [colour.strip() for colour in raw_colours]

    original_colours = clean_colours.copy()
    sorted_colours = sorted(original_colours)

    if original_colours == sorted_colours:
        pytest.fail("The Colour Dropdown options are sorted!!")
    else:
        assert True

def test_animals_dropdown_not_sorted(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    raw_list = page.locator("#animals option").all_text_contents()
    clean_list = [colour.strip() for colour in raw_list]

    original_list = clean_list.copy()
    sorted_list = sorted(original_list)

    if original_list == sorted_list:
        assert True
    else:
        pytest.fail("In the Animals Dropdown options are not in sorted order!!")