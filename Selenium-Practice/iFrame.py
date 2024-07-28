from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://the-internet.herokuapp.com/iframe")

iFrame = browser.find_element(By.ID, value='mce_0_ifr')
browser.switch_to.frame(iFrame)

Text_editor = browser.find_element(By.ID, value='tinymce')
Text_editor.clear()
Text_editor.send_keys("This is Selenium with Python iFrame Tutorial")
time.sleep()

browser.switch_to.default_content()
Selenium_Link = browser.find_element(By.XPath, value='//html')
Selenium_Link.click()