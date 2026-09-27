from playwright.sync_api import Page, expect
from random import choice


def test_farme3_iframe(page:Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    #Access Parent Frame
    frame3 = page.frame(url="https://ui.vision/demo/webtest/frames/frame_3")

    frame3.get_by_role("textbox").fill("Parent Frame")

    #Returns a list of iframes under a frame
    iframe = frame3.child_frames

    iframe[0].get_by_label("I am a human").click()

    checkboxes = iframe[0].locator(".uHMk6b.fsHoPb").all()
    checkbox = choice(checkboxes)
    checkbox.check()

    iframe[0].locator("div[class='uArJ5e UQuaGc YhQJj zo8FOc ctEux'] span[class='NPEfkd RveJvd snByac']").click()

    iframe[0].locator("input.whsOnd.zHQkBf").fill("Short Answer")

    iframe[0].locator("textarea.KHxj8b.tL9Q4c").fill("Long Answer")

    iframe[0].locator('span.NPEfkd.RveJvd.snByac').nth(1).click()