import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

browser = webdriver.Firefox()
browser.get("https://the-internet.herokuapp.com/broken_images")
browser.maximize_window()
images: WebElement = browser.find_element(By.TAG_NAME, value='img')
broken_images = []
for image in images:
    src = image.get_attribute('src')
    if src:
        response = requests.get('src')
        if response.status_code != 200:
            broken_images.append(src)
            print(f'Broken Image Found')

if broken_images:
    print("list of broken image:")
    for broken_image in broken_images:
        print(broken_image)
    else:
        print("No broken image found")