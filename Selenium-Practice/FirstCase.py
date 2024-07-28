from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://selenium.dev/')
browser.maximize_window()
actual_title = browser.title
expected_title = "Selenium"

if actual_title == expected_title:
    print("The title matched")
else:
    print("The title didn't match")
