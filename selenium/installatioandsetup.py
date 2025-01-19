from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Setup Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
driver = webdriver.Chrome(options=chrome_options)

# URL to check
url = "https://www.businesstimes.com.sg/singapore/smes/labubu-co-op-games-vr-how-arcades-are-keeping-patrons-hooked?andbeyondrefresh=1"

# Function to check ad slots and elements with `andbeyond_aduni`
def check_ad_and_div(interval, checks):
    driver.get(url)
    time.sleep(5)  # Wait for the page to load
    
    print("Starting refresh checks...\n")
    
    for i in range(checks):
        print(f"Check #{i + 1}")
        
        # Refresh the page after the first check
        if i > 0:
            print("\nRefreshing the page...\n")
            driver.refresh()
            time.sleep(interval)
        
        # Find all ads with Google ads iframe
        ads = driver.find_elements(By.CSS_SELECTOR, '[id*="google_ads_iframe"]')
        
        print(f"Ads detected: {len(ads)}")
        for ad in ads:
            print(f"Ad Slot ID: {ad.get_attribute('id')} | Ad Source: {ad.get_attribute('src')}")
        
        # After the first refresh, check for divs containing `andbeyond_aduni`
        if i > 0:
            andbeyond_divs = driver.find_elements(By.CSS_SELECTOR, '[class*="andbeyond_aduni"], [id*="andbeyond_aduni"]')
            print(f"\nDivs containing 'andbeyond_aduni': {len(andbeyond_divs)}")
            for div in andbeyond_divs:
                print(f"Div ID: {div.get_attribute('id')}, Div Class: {div.get_attribute('class')}")
        
        print("\n")
    
    print("Refresh checks completed.\n")

# Run the test case with 30-second intervals and 2 refresh checks
check_ad_and_div(interval=30, checks=2)

# Close the browser
driver.quit()
