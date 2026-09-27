from playwright.sync_api import Page, expect

def test_mouse_hover(page:Page):
    page.goto("https://swisnl.github.io/jQuery-contextMenu/demo.html")

    r_click = page.get_by_text("right click me", exact=True)

    r_click.click(button="right")

    page.on("dialog", lambda dialogue:dialogue.accept())
    r_click.locator(".context-menu-list.context-menu-root>li:nth-child(3)")

    page.wait_for_timeout(3000)