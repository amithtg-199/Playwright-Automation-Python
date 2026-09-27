from playwright.sync_api import Page, expect

def test_simple_prompt_func_method(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    alert = []
    def alert_message(dialogue):
        alert.append(dialogue.message)
        dialogue.accept()

    page.on("dialog", alert_message)
    page.get_by_role("button", name="Simple Alert").click()
    assert len(alert) > 0
    assert alert[0] == "I am an alert box!"

def test_simple_prompt_lambda_func(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.on("dialog",lambda dialogue:dialogue.accept())
    page.get_by_role("button", name="Simple Alert").click()

def test_confirmation_alert_accept(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.on("dialog", lambda dialogue:dialogue.accept())
    page.get_by_role("button", name="Confirmation Alert").click()
    output_prompt = page.locator("#demo")
    expect(output_prompt).to_contain_text("OK")

def test_confirmation_alert_cancel(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.on("dialog", lambda dialogue:dialogue.dismiss())
    page.get_by_role("button", name="Confirmation Alert").click()
    output_prompt = page.locator("#demo")
    expect(output_prompt).to_contain_text("Cancel")

def test_prompt_alert_accept(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.on("dialog", lambda dialogue:dialogue.accept("Prompt Check"))
    page.get_by_role("button", name="Prompt Alert").click()
    output_prompt = page.locator("#demo")
    expect(output_prompt).to_contain_text("Prompt Check")

def test_prompt_alert_dismiss(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.on("dialog", lambda dialogue:dialogue.dismiss())
    page.get_by_role("button", name="Prompt Alert").click()
    output_prompt = page.locator("#demo")
    expect(output_prompt).to_contain_text("cancelled")