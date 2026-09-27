from playwright.sync_api import Page, expect

def test_order_by_visible(page: Page):
    page.goto("https://bstackdemo.com/")

    expect(page.get_by_role("combobox")).to_be_visible()

def test_order_by_lowest(page: Page):
    page.goto("https://bstackdemo.com/")

    #Get the first price immediately as the page loads
    initial_first_price = page.locator("div.val b").first.inner_text()

    page.get_by_role("combobox").select_option(value="lowestprice")

    #Wait until the first amount is not the initial loaded amount, i.e. the amount is sorted.
    expect(page.locator("div.val b").first).not_to_have_text(initial_first_price)

    prices_whole = page.locator("div.val b").all_inner_texts()
    prices_decimal = page.locator("div.val span").all_inner_texts()

    actual_price = [float(f"{w}{d}") for w,d in zip(prices_whole, prices_decimal)]
    print(actual_price)
    ascending_price = sorted(actual_price)
    print(ascending_price)
    assert actual_price == ascending_price, (
        f"Products are not sorted in ascending order.\n"
        f"Actual:   {actual_price}\n"
        f"Expected: {ascending_price}"
    )

def test_order_by_highest(page: Page):
    page.goto("https://bstackdemo.com/")

    initial_first_price = page.locator("div.val b").first.inner_text()

    page.get_by_role("combobox").select_option(value="highestprice")

    expect(page.locator("div.val b").first).not_to_have_text(initial_first_price)


    prices_whole = page.locator("div.val b").all_inner_texts()
    prices_decimal = page.locator("div.val span").all_inner_texts()

    actual_price = [float(f"{w}{d}") for w,d in zip(prices_whole, prices_decimal)]
    print(actual_price)
    descending_price = sorted(actual_price, reverse=True)
    print(descending_price)
    assert actual_price == descending_price, (
        f"Products are not sorted in descending order.\n"
        f"Actual:   {actual_price}\n"
        f"Expected: {descending_price}"
    )

def test_print_lowest_highest_price(page:Page):
    page.goto("https://bstackdemo.com/")

    products = []

    for item in page.locator(".shelf-item").all():
        name = item.locator("p.shelf-item__title").inner_text()
        w = item.locator("div.val b").inner_text()
        d = item.locator("div.val span").inner_text()

        products.append((name, float(f"{w}{d}")))

    highest_product = max(products, key=lambda item:item[1])
    loweset_product = min(products, key=lambda item:item[1])
    
    print(f"Highest priced product is: {highest_product[0]} at: {highest_product[1]:.2f}")
    print(f"Lowest priced product is: {loweset_product[0]} at : {loweset_product[1]:.2f}")