from playwright.sync_api import Page, expect

def test_is_table_visible(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    table = page.locator("table[name='BookTable']>tbody")
    expect(table).to_be_visible()

def test_get_column_names_of_table(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    table = page.locator("table[name='BookTable']>tbody")

    l_column = table.locator("tr>th")

    expect(l_column).to_have_count(4)

    l_column_names = l_column.all_inner_texts()
    print("Column names are ===> ", l_column_names)

def test_get_1st_row_values(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    rows = page.locator("table[name='BookTable']>tbody>tr")

    l_first_row = rows.nth(1).locator("td")
    first_row_values = l_first_row.all_inner_texts()
    print("First Row Values are ==> ", first_row_values)
    expect(l_first_row).to_have_text(['Learn Selenium', 'Amit', 'Selenium', '300'])

def test_get_all_table_data_ex_column_name(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    tb_l_data = page.locator("table[name='BookTable']>tbody>tr").all()
    tb_data = [row.locator("td").all_inner_texts() for row in tb_l_data[1:]]
    print(tb_data)

def test_get_book_name_matching(page: Page):
    #To get book name that matches author="Mukesh"
    page.goto("https://testautomationpractice.blogspot.com/")

    all_rows = page.locator("table[name='BookTable']>tbody>tr").all()
    for row in all_rows[1:]:
        author_name = row.locator("td").nth(1).inner_text()
        if author_name =="Mukesh":
            auth_book = row.locator("td").nth(0).inner_text()
            print(f"{author_name}: {auth_book}")

def test_sum_of_all_book_price(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    total_price = 0
    all_rows = page.locator("table[name='BookTable']>tbody>tr").all()
    for row in all_rows[1:]:
        price = int(row.locator("td").nth(3).inner_text())
        total_price+=price
    print("Total Price is: ", total_price)
