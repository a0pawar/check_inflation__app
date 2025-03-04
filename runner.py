from playwright.sync_api import Playwright, sync_playwright, expect
import time

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    # Set a very long timeout for initial page load
    page.set_default_navigation_timeout(120000)  # 2 minutes
    page.set_default_timeout(120000)  # 2 minutes
   
    try:
        # Navigate to the page and add a long sleep to ensure everything is loaded
        page.goto("https://inflation-monitor.onrender.com/")
        time.sleep(10)   
        #page.get_by_label("Username").click()
        #page.get_by_label("Username").fill("PMRD")
        time.sleep(1)
        #page.get_by_label("Password", exact=True).click()
        #page.get_by_label("Password", exact=True).fill("pass123")
        time.sleep(1)
        #page.get_by_test_id("stBaseButton-secondary").click()
        time.sleep(15)  # Wait 30 seconds after initial load
        
        
        # Click just one tab
        #page.get_by_role("tab", name="Arrivals and Wholesale Prices").click()
        time.sleep(10)  # Wait 10 seconds after click
        page.goto("https://financial-markets-dashboard.onrender.com/")
        time.sleep(10)  
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        context.close()
        browser.close()

if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
