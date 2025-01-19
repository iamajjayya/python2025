#1, Python Installed 
# pip install selenium 
# step by step

from selenium import webdriver

#initilaize the webdriver for Chrome
driver =  webdriver.Chrome()


#open a website

driver.get("https://www.google.com")


#print the page  title

print(" Page  title is : ", driver.title)


#close  the  browser

driver.quit()