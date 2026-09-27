from playwright.sync_api import Page, expect

def test_drag_drop(page:Page):
    page.goto("https://demo.guru99.com/test/drag_drop.html")

    d_source = page.locator("a").filter(has_text="5000").nth(1)
    d_target = page.locator("#amt7:visible")

    d_source.drag_to(d_target)

    b_source = page.get_by_text("BANK", exact=True)
    b_target = page.locator("ol[id='bank'] li[class='placeholder']")

    b_source.drag_to(b_target)

    c_source = page.locator("a").filter(has_text="5000").nth(3)
    c_target = page.locator("ol[id='amt8'] li[class='placeholder']")

    c_source.drag_to(c_target)

    s_source = page.get_by_text("SALES", exact=True)
    s_target = page.locator("ol[id='loan'] li[class='placeholder']")

    s_source.drag_to(s_target)

    expect(page.locator("div.table4_result a.button.button-green")).to_have_text("Perfect!")