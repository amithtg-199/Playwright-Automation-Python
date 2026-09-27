from playwright.sync_api import Page, expect
import re

def test_dynamic_table_data_validation(page: Page):
    page.goto("https://practice.expandtesting.com/dynamic-table")

    # Fetch All rows
    rows = page.locator("table.table.table-striped tbody tr").all()

    cpu_load = ""
    for row in rows:
        application_name = row.locator("td").nth(0).inner_text()
        if application_name == "Chrome":
            cpu_load = row.locator("td:has-text('%')").inner_text()
    print("CPU Load for Chrome ==>", cpu_load)
    expect(page.locator("#chrome-cpu")).to_contain_text(cpu_load)

'''Assignment STARTS'''
def test_dynamic_table_cpu_load_validation(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # Get all rows
    rows = page.locator("#taskTable tbody tr").all()
    cpu_usage = ""
    for row in rows:
        applicaton_name = row.locator("td").nth(0).inner_text()
        if applicaton_name == "Chrome":
            cpu_usage = row.locator("td:has-text('%')").inner_text()
    print("Chrome CPU Usage ==>", cpu_usage)
    expect(page.locator(".chrome-cpu")).to_contain_text(cpu_usage)

def test_dynamic_table_memory_firefox_val(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # Get all rows
    rows = page.locator("#taskTable tbody tr").all()
    f_mem_usage = ""
    for row in rows:
        applicaton_name = row.locator("td").nth(0).inner_text()
        if applicaton_name == "Firefox":
            f_mem_usage = row.locator("td", has_text=re.compile(r"MB\s*$")).inner_text()
    print("Firefox Memory Usage ==>", f_mem_usage)
    expect(page.locator(".firefox-memory")).to_contain_text(f_mem_usage)

def test_dynamic_table_netwrok_chrome_val(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # Get all rows
    rows = page.locator("#taskTable tbody tr").all()
    network_speed = ""
    for row in rows:
        applicaton_name = row.locator("td").nth(0).inner_text()
        if applicaton_name == "Chrome":
            network_speed = row.locator("td", has_text=re.compile(r"Mbps\s*$")).inner_text()
    print("Chrome Network Speed ==>", network_speed)
    expect(page.locator(".chrome-network")).to_contain_text(network_speed)

def test_dynamic_table_disk_space_firefox_val(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # Get all rows
    rows = page.locator("#taskTable tbody tr").all()
    disk_space = ""
    for row in rows:
        applicaton_name = row.locator("td").nth(0).inner_text()
        if applicaton_name == "Firefox":
            disk_space = row.locator("td", has_text=re.compile(r"MB/s\s*$")).inner_text()
    print("Firefix Disk Space ==>", disk_space)
    expect(page.locator(".firefox-disk")).to_contain_text(disk_space)
