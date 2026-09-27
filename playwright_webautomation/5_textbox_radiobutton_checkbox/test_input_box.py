from playwright.sync_api import Page, expect

def test_input_box_name_visible_enabled(page: Page):
    page.goto("")

    name = page.locator("input.form-control#name")

    expect(name).to_be_visible()
    expect(name).to_be_enabled()

def test_name_max_length(page: Page):
    page.goto("")

    name = page.locator("input.form-control#name")

    #get_attribute is used to get the data from DOM for the locator and print
    print("Max-length of Name field is: ", name.get_attribute("maxlength"))
    expect(name).to_have_attribute(name="maxlength",value="15")

def test_invalid_length_name(page:Page):
    page.goto("")

    name = page.locator("input.form-control#name")

    long_name = "sdkasdksaddsadsdadiwwdiddwdwqj"
    name.fill(long_name)
    #Here input_value() returns the actual value inserted into the text box.
    print(f"Name value sent is {long_name}, Actual name inserted to text-box: {name.input_value()}")
    expect(name).to_have_value(long_name[:15])