from playwright.sync_api import Page, expect
import pytest

def test_success_1(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    expect(page).to_have_url("https://testautomationpractice.blogspot.com/")

def test_succee_2(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.get_by_role("link", name="PlaywrightPractice").click()
    expect(page).to_have_url("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")

def test_error(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    expect(page.locator("p.description")).to_contain_text("Java", ignore_case=True)
