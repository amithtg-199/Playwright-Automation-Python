"""Expected Output:
• The number of suggestions should be printed in the terminal.
• The 5th suggestion (if available) should be displayed.
• All suggestions should be listed in the output.
• If "smartphone" appears, it should be automatically clicked.
"""

from playwright.sync_api import Page, expect
import re

def test_flipkart_count_of_auto_suggestion(page: Page):
    page.goto("https://www.flipkart.com/")

    #close the login pop-up
    page.locator("div>span.b3wTlE").click()

    #Locate smart in search box
    search_box = page.locator("input.nw1UBF.v1zwn26:visible")

    #enter "smart" in search box
    search_box.fill("smart")

    #Get count of all elements
    suggestions = page.locator("div.VDtK0l._1psv1ze2u._1psv1ze53._1psv1ze9x._1psv1ze7o")
    suggestions.first.wait_for(state="visible")
    count = suggestions.count()
    expect(suggestions).to_have_count(count=count)

    #select the sugesstion that matches smartphone
    all_suggestions = [text.split('\n')[0].strip() for text in suggestions.all_inner_texts()]
    selection = next(((idx, val) for idx, val in enumerate(all_suggestions) if val == "smartphone" ), None)
    suggestions.nth(selection[0]).click()
    page.wait_for_timeout(3000)
    expect(page).to_have_url(re.compile(r"smartphone"))






