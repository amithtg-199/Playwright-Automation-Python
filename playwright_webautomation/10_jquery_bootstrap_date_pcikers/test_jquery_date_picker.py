from playwright.sync_api import Page, expect

#Helper function
def _select_date_jquery(page:Page, target_year, target_month, tearget_day, is_future):
    while True:
        current_month = page.locator(".ui-datepicker-month").inner_text()
        current_year = page.locator(".ui-datepicker-year").inner_text()
        if current_month == target_month and current_year == target_year:
            break

        if is_future == True:
            page.locator(".ui-datepicker-next.ui-corner-all span").click()
        else:
            page.locator(".ui-datepicker-prev.ui-corner-all span").click()
    #All date locators
    days = page.locator(".ui-datepicker-calendar tbody td").all()

    for day in days:
        day_text = day.inner_text()
        if day_text == tearget_day:
            day.click()
            break
        

def test_simple_jquery_fill(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #mm/dd/yyyy format
    date = page.locator("#datepicker")
    date.fill("09/14/2026")

    expect(date).to_have_value("09/14/2026")

def test_jquery_select_date(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    date = page.locator("#datepicker")
    date.click()
    year = "2027"
    month = "October"
    day = "30"
    #To mention to if the provided date is of future or present
    is_future = True
    _select_date_jquery(page, year, month, day, is_future)

    print("Selected date: ", date.input_value())

    #Assert if the date is correct
    expect(date).to_have_value("10/30/2027")