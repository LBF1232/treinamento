from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('file:///app/treinamento-perifericos.html')

    # Click next 6 times to go through all steps
    for i in range(6):
        page.click('#nextBtn')
        page.wait_for_timeout(500)

    page.screenshot(path='verification.png')
    browser.close()
