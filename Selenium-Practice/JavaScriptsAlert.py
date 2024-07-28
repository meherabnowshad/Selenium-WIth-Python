from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Firefox()
browser.maximize_window()
url = "https://the-internet.herokuapp.com/javascript_alerts"
browser.get(url)
AlertButton = browser.find_element(By.XPATH, value="//button[normalize-space()='Click for JS Prompt']")
AlertButton.click()
alert = browser.switch_to.alert
alert.send_keys("This is Selenium with Python Tutorial")
alert.accept()
# time.sleep(5)