from playwright.sync_api import Page, expect

def test_get_count_of_flights_b_l(page:Page):
    page.goto("https://blazedemo.com/index.php")

    page.locator("[name='fromPort']").select_option(value="Boston")
    page.locator("[name='toPort']").select_option(value="London")

    page.get_by_role("button").click()
    expect(page).to_have_url("https://blazedemo.com/reserve.php")

    count_of_flights = page.locator(".table tbody tr").count()

    expect(page.locator(".btn.btn-small")).to_have_count(count_of_flights)

def test_book_flight_boston_london(page:Page):
    page.goto("https://blazedemo.com/index.php")

    #Select Boston to London ------------------------
    page.locator("[name='fromPort']").select_option(value="Boston")
    page.locator("[name='toPort']").select_option(value="London")

    page.get_by_role("button").click()
    expect(page).to_have_url("https://blazedemo.com/reserve.php")

    #Select Cheapest flight ----------------------------
    rows = page.locator(".table tbody tr").all()
    prices = []
    for row in rows:
        raw_price = row.locator("td").nth(5).inner_text()
        clean_price = float(raw_price.replace("$", "").strip())
        prices.append(clean_price)

    min_flight_fare = min(prices)
    cheapest_row_index = prices.index(min_flight_fare)
    
    print(f"Cheapest price: ${min_flight_fare} at row index {cheapest_row_index}")
    
    rows[cheapest_row_index].locator("td").nth(0).get_by_role("button").click()

    expect(page).to_have_url("https://blazedemo.com/purchase.php")

    #Fill details and submit---------------
    page.get_by_label("Name", exact=True).fill("Test")
    page.get_by_role("textbox", name="Address").fill("1, 2nd main")
    page.get_by_role("textbox", name="City").fill("Manchester")
    page.get_by_role("textbox", name="State").fill("london")
    page.get_by_role("textbox", name="Zip Code").fill("1234")
    page.get_by_role("combobox").select_option(value="visa")
    page.get_by_role("textbox", name="Credit Card Number").fill("1217261826")
    page.get_by_role("textbox", name="Month").fill("12")
    page.get_by_role("textbox", name="Year").fill("2026")
    page.get_by_role("textbox", name="Name on Card").fill("Jason Bourne")
    page.get_by_role("checkbox").check()
    page.locator("input.btn.btn-primary").click()

    #Confirm Registration
    expect(page).to_have_url("https://blazedemo.com/confirmation.php")

    #Assert Registration
    expect(page.locator("h1")).to_contain_text("purchase")