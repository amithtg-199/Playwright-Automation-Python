from playwright.sync_api import Playwright, expect
import os
from datetime import datetime

def test_pw_tracing(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    timestamp = datetime.now().strftime(r"%d%m%Y%H%M%S")
    os.makedirs("traces", exist_ok=True)

    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    try:
        page.goto("https://www.demoblaze.com/index.html")
        page.get_by_role("link", name="Log in").click()
        page.locator("#loginusername").fill("pavanol")
        page.locator("#loginpassword").fill("test@123")
        page.get_by_role("button", name="Log in").click()
        logo = page.get_by_role("link", name="PRODUCT STORE")
        logo.first.wait_for(state="visible")

        page.get_by_role("link", name="Laptops").click()

        expect(page.locator(".hrefch", has_text='Sony vaio i5')).to_be_visible()
        l_all_laptop_data = []
        
        while True:
            l_laptops = page.locator("#tbodyid [class='col-lg-4 col-md-6 mb-4']").all()
            for pc in l_laptops:
                title = pc.locator(".card-title").inner_text().strip()
                price_text = pc.locator("h5").inner_text().strip()
                clean_price = float(price_text.replace("$", "").replace(",", ""))
                
                # Target the clickable link inside the card element, not the card container itself
                link_element = pc.locator(".hrefch")
                
                l_all_laptop_data.append({
                    "title": title,
                    "price": clean_price,
                    "element": link_element # Store the specific link element to click later
                })
                
            next_button = page.locator("button:has-text('Next')").first

            if next_button.is_visible():
                page.locator("button:has-text('Next')").click()
                page.wait_for_timeout(1000) 
            else:
                break

        print(f"Total Laptops data collected: {len(l_all_laptop_data)}")

        cheapest_pc = min(l_all_laptop_data, key=lambda x: x["price"])
        print(f"Cheapest is {cheapest_pc['title']} at ${cheapest_pc['price']}")
        
        # Click using the stored locator element from the dictionary
        cheapest_pc["element"].click()

        # Register dialog listener BEFORE clicking Add to cart
        page.on("dialog", lambda dialog: dialog.accept())
        page.get_by_role("link", name="Add to cart").click()
        
        # Small wait to ensure cart action completes before tracing stops
        page.wait_for_timeout(2000)

    finally:
        trace_path = f"traces/results_{timestamp}.zip"
        context.tracing.stop(path=trace_path)
        print(f"Trace saved successfully at: {trace_path}")
        context.close()
        browser.close()