from playwright.sync_api import Page, expect

def test_radio_button_check_male(page:Page):

    page.goto("")
    male_radio = page.get_by_role("radio", name="Male", exact=True)

    expect(male_radio).to_be_visible()
    expect(male_radio).to_be_enabled()

    expect(male_radio).not_to_be_checked()

    male_radio.check()

    expect(male_radio).to_be_checked()