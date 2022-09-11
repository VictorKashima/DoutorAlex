from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.youtube.com/")
    page.fill("input[id='search']", "SAVEIRO REBAIXADA")
    page.click("button[id='search-icon-legacy']")
    print(page.title())
    page.wait_for_timeout(5000)
    # browser.close()