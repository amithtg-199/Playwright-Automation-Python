from playwright.sync_api import Page, expect

def test_total_frames_in_webpage(page:Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    list_frame = page.frames

    print(f"The Webpage has {len(list_frame)} frames")

def test_fram1_simple_frame(page:Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    #Access Fram1
    frame1 = page.frame(url="https://ui.vision/demo/webtest/frames/frame_1")

    # Interact With element of Fram1
    f1_text_box = frame1.get_by_role("textbox")
    f1_text_box.fill("Welcome")

    # Assert the fram1 element to have the input value
    expect(f1_text_box).to_have_value("Welcome")

def test_fram2_simple_frame(page:Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    #Access Fram1
    frame2 = page.frame(url="https://ui.vision/demo/webtest/frames/frame_2")

    # Interact With element of Fram1
    f2_text_box = frame2.get_by_role("textbox")
    f2_text_box.fill("Welcome to F2")

    # Assert the fram1 element to have the input value
    expect(f2_text_box).to_have_value("Welcome to F2")

def test_fram4_simple_frame(page:Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    #Access Fram1
    frame4 = page.frame(url="https://ui.vision/demo/webtest/frames/frame_4")

    # Interact With element of Fram1
    f4_text_box = frame4.get_by_role("textbox")
    f4_text_box.fill("Welcome to F4")

    # Assert the fram1 element to have the input value
    expect(f4_text_box).to_have_value("Welcome to F4")
    
