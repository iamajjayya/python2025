from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver
driver = webdriver.Chrome()

# Open the login page
driver.get("https://support.orangehrm.com/portal/en/signin")

try:
    # Wait for the username field to be present
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    
    # Locate the username and password fields
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    
    # Enter credentials
    username.send_keys("ajjayya2002@gmail.com")
    password.send_keys("789Ajay@123")
    
    # Locate and click the Sign In button
    login_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".signin-button"))  # Update the selector based on the actual button
    )
    login_button.click()
    
    # Wait for a moment to observe the result (optional)
    WebDriverWait(driver, 10).until(
        EC.url_changes("https://support.orangehrm.com/portal/en/signin")
    )
    print("Login successful!")
    
except Exception as e:
    print("An error occurred:", e)

finally:
    # Quit the browser
    driver.quit()
