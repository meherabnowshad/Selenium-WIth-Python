from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/dropdown")

dropdown_element = driver.find_element(By.ID, value="dropdown")
select = Select(dropdown_element)
# option_count = len(select.options)
# expect_count = 3

target_value = "Option 2"

for i in select.options:
    if i.text == target_value:
        i.click()
        print(f"Selected option is {target_value}")
        break
    else:
        print(f'{target_value} not found')

# if option_count == expect_count:
#     print("Test case passed. Count is correct")
# else:
#     print("Test case failed. Count is incorrect")

# dropdown_element.select_by_visible_text("Option 2")
dropdown_element.select_by_index(2)
# select.select_by_value("2")
