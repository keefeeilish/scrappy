from playwright.sync_api import sync_playwright

def fetch_js(url, wait_for_selector=None, timeout=15000):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=timeout)

        if wait_for_selector:
            page.wait_for_selector(wait_for_selector, timeout=timeout)

        html = page.content()
        browser.close()
        return html
