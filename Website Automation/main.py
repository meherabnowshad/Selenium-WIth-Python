import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()

phones = driver.find_element(By.XPATH, value='//a[text()="Phones & PDAs"]')
phones.click()
# time.sleep(3)

# iphone = driver.find_element(By.XPATH, value='//a[text()="iPhone"]')
# iphone.click()
# # time.sleep(3)
#
# first_picture = driver.find_element(By.XPATH, value='//ul[@class="thumbnails"]/li[1]')
# first_picture.click()
# # time.sleep(3)
#
# next_click = driver.find_element(By.XPATH, value='//button[@title="Next (Right arrow key)"]')
# for i in range(0,5):
#     next_click.click()
#     # time.sleep(2)
#
# driver.save_screenshot("screenshot"+str(random.randint(0,101))+".png")
# # time.sleep(2)
#
# driver.find_element(By.XPATH, value='//button[@title="Close (Esc)"]').click()
#
# iphone_quantity = driver.find_element(By.ID,value='input-quantity')
# iphone_quantity.click()
# # time.sleep(1)
#
# iphone_quantity.clear()
# iphone_quantity.send_keys('2')
# # time.sleep(1)
#
# add_to_cart = driver.find_element(By.ID,value="button-cart")
# add_to_cart.click()
# # time.sleep(2)

laptop_section = driver.find_element(By.XPATH, value='//a[text()="Laptops & Notebooks"]')
laptop_section.click()

laptop_section_2 = driver.find_element(By.XPATH, value='//a[text()="Show AllLaptops & Notebooks"]')
laptop_section_2.click()
# time.sleep(2)

hp_laptop = driver.find_element(By.XPATH, value='//a[text()="HP LP3065"]')
hp_laptop.click()

add_to_cart_laptop = driver.find_element(By.ID, value='button-cart')

add_to_cart_laptop.location_once_scrolled_into_view
# time.sleep(2)

calendar_button = driver.find_element(By.XPATH, value='//i[@class="fa fa-calendar"]')
calendar_button.click()
# time.sleep(1)

next_click_calender = driver.find_element(By.XPATH,value='//th[@class="next"]')
month_year = driver.find_element(By.XPATH,value='//th[@class="picker-switch"]')

while month_year.text != 'December 2022':
    next_click_calender.click()
# time.sleep(2)

calendar_date = driver.find_element(By.XPATH,value='//td[text()="31"]')
calendar_date.click()
# time.sleep(2)

add_to_cart_laptop.click()

cart_total = driver.find_element(By.ID, value='cart-total')
cart_total.click()
checkout = driver.find_element(By.XPATH, value='//i[@class="fa fa-share"]')
checkout.click()
checkout = driver.find_element(By.XPATH, value='//i[@class="fa fa-caret-down"]')
checkout.click()

guest = driver.find_element(By.XPATH, value='//input[@value="guest"]')
guest.click()
continue_guest = driver.find_element(By.ID, value='button-account')
continue_guest.click()

billing_details = driver.find_element(By.XPATH, value='//div[@class="panel-body"]')
# billing_details.location_once_scrolled_into_view

checkout_first = driver.find_element(By.ID, value="input-payment-firstname")
checkout_first.click()
checkout_first.send_keys('Meherab Hossain')

checkout_last = driver.find_element(By.ID, value='input-payment-lastname')
checkout_last.click()
checkout_last.send_keys('Nowshad')

checkout_email = driver.find_element(By.ID, value='input-payment-email')
checkout_email.click()
checkout_email.send_keys('meherabhossainnowshad@gmail.com')

checkout_telephone = driver.find_element(By.ID, value='input-payment-telephone')
checkout_telephone.click()
checkout_telephone.send_keys('+8801953925305')

checkout_telephone = driver.find_element(By.ID, value='input-payment-telephone')
checkout_telephone.click()
checkout_telephone.send_keys('+8801953925305')

checkout_address1 = driver.find_element(By.ID, value='input-payment-address-1')
checkout_address1.click()
checkout_address1.send_keys('Bangladesh')

checkout_city = driver.find_element(By.ID, value='input-payment-city')
checkout_city.click()
checkout_city.send_keys('Dhaka')

checkout_postal_Code = driver.find_element(By.ID, value='input-payment-postcode')
checkout_postal_Code.click()
checkout_postal_Code.send_keys('1400')

checkout_country = driver.find_element(By.ID, value='input-payment-country')
checkout_country.click()

checkout_country_name = driver.find_element(By.XPATH, value='//option[@value="18"]')
checkout_country_name.click()

checkout_country_region = driver.find_element(By.ID, value='input-payment-zone')
checkout_country_region.click()

checkout_country_region_name = driver.find_element(By.XPATH, value='//option[@value="322"]')
checkout_country_region_name.click()

continue_billing = driver.find_element(By.ID, value='button-guest')
continue_billing.click()

driver.find_element(By.XPATH, value="//input[@class=\"btn btn-primary\"]").click()

terms = driver.find_element(By.XPATH, value='//input[@name="agree"]')
terms.click()

payment_method_continue = driver.find_element(By.ID, value='button-payment-method')
payment_method_continue.click()

confirm_button = driver.find_element(By.ID, value='button-confirm')
confirm_button.click()

driver.close()