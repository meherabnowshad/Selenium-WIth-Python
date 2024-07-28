from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://the-internet.herokuapp.com/nested_frames")


browser.switch_to.frame("frame-top")

browser.switch_to.frame("frame-middle")

content = browser.find_element(By.ID, value='content').text
print("Content in middle frame", content)

browser.switch_to.default_content()

browser.switch_to.frame("frame-bottom")
content_Bottom = browser.find_element(By.TAG_NAME, value = 'body').text
print("Content in Bottom frame",content_Bottom)

