from playwright.sync_api import Page, expect

def test_verifyPageUrl(page: Page):
    page.goto("https://the-internet.herokuapp.com/") #Opening a Web URL
    print("URL is: ", page.url)
    expect(page).to_have_url("https://the-internet.herokuapp.com/") #Asserting if URL is opened or not

def test_verify_title(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    print(f"For the Url: {page.url}, the title is: {page.title()}")
    expect(page).to_have_title("The Internet")



