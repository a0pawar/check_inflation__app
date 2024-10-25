from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)  # Changed to headless=True
    context = browser.new_context()
    page = context.new_page()
   
    # Navigate to the page and wait for it to be fully loaded
    page.goto("https://inflation-monitor.onrender.com/")
    # Wait for network to be idle and page to be fully loaded
    page.wait_for_load_state("networkidle")
    page.wait_for_load_state("domcontentloaded")
   
    # Wait for the first tab to be visible and clickable
    wholesale_tab = page.get_by_role("tab", name="Wholesale Prices and Arrivals")
    wholesale_tab.wait_for(state="visible")
    wholesale_tab.click()
   
    # Add small delays between tab clicks to ensure content loads
    page.wait_for_timeout(5000)
    page.get_by_role("tab", name="Agricultural Production Trends").click()
   
    page.wait_for_timeout(5000)
    page.get_by_role("tab", name="Rainfall Deviation").click()
   
    page.wait_for_timeout(2000)
    page.get_by_role("tab", name="DCA Retail Price Trends").click()
   
    page.wait_for_timeout(2000)
    page.get_by_role("tab", name="Rainfall Deviation").click()
   
    # ---------------------
    context.close()
    browser.close()

if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)