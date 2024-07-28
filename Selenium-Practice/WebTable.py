from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get("https://cosmocode.io/automation-practice-webtable/")
browser.maximize_window()
browser.execute_script("window.scrollTo(0,700)")
table = browser.find_element(By.ID, value='countries')
rows = table.find_element(By.TAG_NAME, value='tr')
target_value = "Australia"
found = False
for row in rows:
    cells = row.find_elements(By.TAG_NAME, value="td")
    for cell in cells:
        if target_value in cell.text:
            print(f'Found Value:{target_value}')
            found = True
            break
        if found:
            break
if not found:
    print(f'Target value"{target_value}" not found')
