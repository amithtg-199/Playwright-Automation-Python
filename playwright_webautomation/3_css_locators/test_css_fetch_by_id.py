from playwright.sync_api import Page, expect

def test_verify_search_data(page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    #Tag= input, id=small-searchterms
    page.locator("input#small-searchterms").fill("Computing and Internet")

    #Click on search button
    page.locator("input.button-1.search-box-button").click()

    #Verify if the data is properly loaded.
    expect(page.get_by_text("Computing and Internet", exact=True)).to_be_visible()