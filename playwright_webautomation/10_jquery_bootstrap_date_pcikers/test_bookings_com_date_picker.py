from playwright.sync_api import Page, expect

ACTUAL_ADULT_TRAVELLERS = 4
ACTUAL_CHILDREN_TRAVELLERS = 2
ACTUAL_ROOM_NUM = 3
IS_WORK = False
IS_PETS = True
YEAR_TRAVEL = "2026"
YEAR_RETRUN = "2026"
MONTH_TRAVEL = "November"
MONTH_RETRUN = "December"
DAY_TRAVEL = "15"
DAY_RETRUN = "20"

def _select_checkin_date(page:Page, year, month, day):
    while True:
        current_month, current_year = page.locator('.e7addce19e.af236b7586').nth(0).inner_text().split(" ")
        if current_year == year and current_month == month:
            break
        else:
            page.get_by_role("button", name="Next month").click()

    left_calendar = page.locator('table[role="grid"]').nth(0)

    l_dates = left_calendar.locator('td[role="gridcell"]:not([aria-disabled="true"])').all()

    for date in l_dates:
        date_text = date.text_content().strip()
        
        if date_text == str(day):
            date.click()
            break


def _select_checkout_date(page:Page, year, month, day):
    while True:
        current_month, current_year = page.locator('.e7addce19e.af236b7586').nth(1).inner_text().split(" ")
        if current_year == year and current_month == month:
            break
        else:
            page.get_by_role("button", name="Next month").click()

    right_calendar = page.locator('table[role="grid"]').nth(1)

    r_dates = right_calendar.locator('td[role="gridcell"]:not([aria-disabled="true"])').all()

    for date in r_dates:
        date_text = date.text_content().strip()
        
        if date_text == str(day):
            date.click()
            break
    page.wait_for_timeout(3000)


def test_check_reservations_paris(page:Page):
    page.goto("https://www.booking.com/")
    #Cloase the pop up
    page.locator("//button[@aria-label='Dismiss sign-in info.']//span[@class='fc70cba028 ca6ff50764']//*[name()='svg']").click()

    # Enter distination
    page.get_by_role("combobox", name="Enter destination").fill("Paris")

    #Click on date selector
    page.locator(".a9b08830eb span.e2c61484ab").click()

    _select_checkin_date(page, year=YEAR_TRAVEL, month=MONTH_TRAVEL, day=DAY_TRAVEL)

    _select_checkout_date(page, year=YEAR_RETRUN, month=MONTH_RETRUN, day=DAY_RETRUN)

    #select ocupants
    page.get_by_test_id("occupancy-config").click()


    #print("Adults Travellers: ", current_adult_travellers)
    while True:
        #Number of Adults
        current_adult_travellers = int(page.locator(".d19a074fcf#group_adults").get_attribute("aria-valuenow"))

        if current_adult_travellers == ACTUAL_ADULT_TRAVELLERS:
            break
        elif current_adult_travellers > ACTUAL_ADULT_TRAVELLERS:
            #Decrement
            page.locator("div.e301a14002").locator("button").nth(0).click()
        else:
            #Increment
            page.locator("div.e301a14002").locator("button").nth(1).click()

    while True:
        current_children_travellers = int(page.locator(".d19a074fcf#group_children").get_attribute("aria-valuenow"))
        if current_children_travellers == ACTUAL_CHILDREN_TRAVELLERS:
            if current_children_travellers > 0:
                for i in range(current_children_travellers):
                    page.locator(".ed4d3c8194[name='age']").nth(i).select_option(value="1")
            break
        elif current_children_travellers > ACTUAL_CHILDREN_TRAVELLERS:
            page.locator("div.e301a14002").locator("button").nth(2).click()
        else:
            page.locator("div.e301a14002").locator("button").nth(3).click()

        

    while True:
        current_num_rooms = int(page.locator(".d19a074fcf#no_rooms").get_attribute("aria-valuenow"))
        if current_num_rooms == ACTUAL_ROOM_NUM:
            break
        elif current_num_rooms > ACTUAL_ROOM_NUM:
            page.locator("div.e301a14002").locator("button").nth(4).click()
        else:
            page.locator("div.e301a14002").locator("button").nth(5).click()

    if IS_WORK == True:
        page.locator(".e6c1c19aa4[for='travelPurpose']>span.bc7af14f80").click()

    if IS_PETS == True:
        page.locator(".e6c1c19aa4[for='pets']>span.bc7af14f80").click()

    page.get_by_role("button", name="Done").click()

    page.get_by_text("Search", exact=True).click()

    expect(page.locator("h1[aria-label*='Paris']")).to_be_visible()

