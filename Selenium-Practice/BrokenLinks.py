from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from urllib3.util import request

driver = webdriver.Firefox()
driver.get("https://jquery.com/")

all_links = driver.find_elements(By.TAG_NAME, value= 'a')
print(f'Total number of links on the page is {len(all_links)}')

for link in all_links:
    href = link.get_attribute("href")
    response = request.get(href)
    if response.status_code >= 400:
        print(f"Broken link: {href}(Status code: {response.status_code})")


    