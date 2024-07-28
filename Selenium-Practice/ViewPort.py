from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
viewports = [(1024,768),(768,1024),(375,667)]

try:
    for width,height in viewports:
        driver.set_window_size(width, height)
        time.sleep(3)
finally:
    driver.close()