from playwright.sync_api import Page, expect

def test_pagination_get_all_content(page: Page):
    page.goto("https://datatables.net/examples/core/basic_init/zero_configuration.html")

    to_continue = True
    while to_continue:
        #Get all rows
        rows = page.locator("table tbody>tr").all()

        for row in rows:
            row_text = row.inner_text()
            print(row_text)

        # Check if the next button is valid
        next_button = page.locator("button[aria-label='Next']")
        is_diabled = next_button.get_attribute("class")
        if "disabled" in is_diabled:
            to_continue = False
        else:
            next_button.click()

def test_dropdown_count_values(page:Page):
    page.goto("https://datatables.net/examples/core/basic_init/zero_configuration.html")

    dropdown = page.locator("#dt-length-0")

    dropdown.select_option(value="10")
    expect(page.locator("#example tbody>tr")).to_have_count(10)

    dropdown.select_option(value="25")
    expect(page.locator("#example tbody>tr")).to_have_count(25)

#Assignment
def test_pagination_select_all_elements(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    rows = page.locator("#productTable tbody tr").all()
# #productTable tbody tr td>input[type='checkbox']

    for i in range(4):
        page.locator("#pagination a[href='#']").nth(i).click()  
        for row in rows:
            name = row.locator("td").nth(1).inner_text()
            price = row.locator("td").nth(2).inner_text()
            print(f"Selecting {name}: for price {price}..")
            checkbox = row.locator("td>input[type='checkbox']")
            if checkbox.is_checked():
                checkbox.uncheck()
            else:
                checkbox.check()

def test_pagination_select_specific_element(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    rows = page.locator("#productTable tbody tr").all()
# #productTable tbody tr td>input[type='checkbox']

    for i in range(4):
        page.locator("#pagination a[href='#']").nth(i).click()  
        for row in rows:
            name = row.locator("td").nth(1).inner_text()
            price = row.locator("td").nth(2).inner_text()
            if name == "VR Headset" and price == "$11.99":
                print(f"Selecting {name}: for price {price}..")
                checkbox = row.locator("td>input[type='checkbox']")
                if checkbox.is_checked():
                    checkbox.uncheck()
                else:
                    checkbox.check()


    