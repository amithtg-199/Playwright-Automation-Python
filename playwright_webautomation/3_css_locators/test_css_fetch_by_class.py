from playwright.sync_api import Page, expect

def test_verify_search_data(page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    #Tag= input, id=small-searchterms
    #page.locator("input.search-box-text.ui-autocomplete-input").fill("Computing and Internet")
    #Also can be written without tag.
    page.locator(".search-box-text.ui-autocomplete-input").fill("Computing and Internet")
    
    #Click on search button without tag
    page.locator(".button-1.search-box-button").click()

    #Verify if the data is properly loaded.
    expect(page.get_by_text("Computing and Internet", exact=True)).to_be_visible()