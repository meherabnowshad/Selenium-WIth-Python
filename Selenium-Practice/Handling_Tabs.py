from datetime import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://www.selenium.dev/")
time.sleep(3)
browser.switch_to.new_window()
browser.get("https://playwright.dev/")
time.sleep(3)
number_of_tabs = len(browser.window_handles)
print(number_of_tabs)
tabs_value = browser.window_handles
print(tabs_value)
Current_tab = browser.current_window_handle
print(Current_tab)
browser.find_element(By.CSS_SELECTOR, value='.getStarted_Sjon').click()
FirstTab = browser.window_handles[0]
if Current_tab != FirstTab:
    browser.switch_to.window(FirstTab)
browser.find_element(By.jQuery, value='$("body > header:nth-child(1) > nav:nth-child(1) > div:nth-child(3) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1) > span:nth-child(1)")').click()