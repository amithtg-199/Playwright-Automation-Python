import asyncio
from playwright.async_api import async_playwright, expect
import pytest

@pytest.mark.asyncio
async def test_verify_url(): #Here we cannot call Page object direct as we cannot open broswer directly since its Async.
    async with async_playwright() as p:
        browser = await p.chromium.launch() #Here we are intializing a new Chromium browser.
        new_page = await browser.new_page() #Here we are defining a new Chrome Page.
        await new_page.goto("https://the-internet.herokuapp.com/")
        my_url = new_page.url
        print("My url is: ", my_url)
        await expect(new_page).to_have_url("https://the-internet.herokuapp.com/")