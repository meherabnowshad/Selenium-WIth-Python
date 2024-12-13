import time
from random import random

from selenium import webdriver
import random
import os

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Firefox()
driver.get("https://tutorialsninja.com/demo/")

# driver.maximize_window()

phones = driver.find_element(By.XPATH, '//a[text()="Phones & PDAs"]')
phones.click()

iphone = driver.find_element(By.XPATH, '//a[text()="iPhone"]')
iphone.click()

first_pic = driver.find_element(By.XPATH, '//ul[@class="thumbnails"]/li[1]')
first_pic.click()

next_click = driver.find_element(By.XPATH,'//button[@title="Next (Right arrow key)"]')

for i in range(0,5):
    next_click.click()
    # time.sleep(1)

driver.save_screenshot("screenshot"+str(random.randint(0,101))+'.png')

close = driver.find_element(By.XPATH, '//button[@title="Close (Esc)"]')
close.click()

quantity = driver.find_element(By.ID, 'input-quantity')
quantity.click()
quantity.clear()
quantity.send_keys(2)

# add_to_cart = driver.find_element(By.ID, "button-cart")
# add_to_cart.click()

laptop = driver.find_element(By.XPATH, '//a[text()="Laptops & Notebooks"]')
laptop.click()

show_all = driver.find_element(By.XPATH, '//a[text()="Show AllLaptops & Notebooks"]')
show_all.click()

hp = driver.find_element(By.XPATH, '//a[text()="HP LP3065"]')
hp.click()

add_to_cart_laptop = driver.find_element(By.ID, 'button-cart')

add_to_cart_laptop.location_once_scrolled_into_view
time.sleep(2)

calendar_button = driver.find_element(By.XPATH, '//i[@class="fa fa-calendar"]')
calendar_button.click()
time.sleep(1)

next_click_calender = driver.find_element(By.XPATH,'//th[@class="next"]')
month_year = driver.find_element(By.XPATH,'//th[@class="picker-switch"]')

while month_year.text != 'December 2022':
    next_click_calender.click()
time.sleep(2)

calendar_date = driver.find_element(By.XPATH,'//td[text()="31"]')
calendar_date.click()
time.sleep(2)

add_to_cart_laptop.click()

cart_total = driver.find_element(By.ID, 'cart-total')
cart_total.click()
checkout = driver.find_element(By.XPATH, '//i[@class="fa fa-share"]')
checkout.click()

checkout = driver.find_element(By.XPATH, '//i[@class="fa fa-caret-down"]')
checkout.click()

guest = driver.find_element(By.XPATH, '//input[@value="guest"]')
guest.click()
continue_guest = driver.find_element(By.ID, 'button-account')
continue_guest.click()

billing_details = driver.find_element(By.XPATH, '//div[@class="panel-body"]')
billing_details.location_once_scrolled_into_view

checkout_first = driver.find_element(By.ID, "input-payment-firstname")
checkout_first.click()
checkout_first.send_keys('Meherab Hossain')

checkout_last = driver.find_element(By.ID, 'input-payment-lastname')
checkout_last.click()
checkout_last.send_keys('Nowshad')

checkout_email = driver.find_element(By.ID, 'input-payment-email')
checkout_email.click()
checkout_email.send_keys('meherabhossainnowshad@gmail.com')

checkout_telephone = driver.find_element(By.ID, 'input-payment-telephone')
checkout_telephone.click()
checkout_telephone.send_keys('+8801953925305')

checkout_telephone = driver.find_element(By.ID, 'input-payment-telephone')
checkout_telephone.click()
checkout_telephone.send_keys('+8801953925305')

checkout_address1 = driver.find_element(By.ID, 'input-payment-address-1')
checkout_address1.click()
checkout_address1.send_keys('Bangladesh')

checkout_city = driver.find_element(By.ID, 'input-payment-city')
checkout_city.click()
checkout_city.send_keys('Dhaka')

checkout_postal_Code = driver.find_element(By.ID, 'input-payment-postcode')
checkout_postal_Code.click()
checkout_postal_Code.send_keys('1400')

checkout_country = driver.find_element(By.ID, 'input-payment-country')
checkout_country.click()

checkout_country_name = driver.find_element(By.XPATH, '//option[@value="18"]')
checkout_country_name.click()

checkout_country_region = driver.find_element(By.ID, 'input-payment-zone')
checkout_country_region.click()

checkout_country_region_name = driver.find_element(By.XPATH, '//option[@value="322"]')
checkout_country_region_name.click()

continue_billing = driver.find_element(By.ID, 'button-guest')
continue_billing.click()

continue_delivery = driver.find_element(By.XPATH, '//input[@id="button-shipping-method"]')
continue_delivery.click()

terms = driver.find_element(By.XPATH, '//input[@name="agree"]')
driver.execute_script("arguments[0].scrollIntoView(true);", terms)
terms.click()


class ActionChains:
    pass


actions = ActionChains(driver)
actions.move_to_element(terms).click().perform()


payment_method_continue = driver.find_element(By.ID, 'button-payment-method')
payment_method_continue.click()

confirm_button = driver.find_element(By.ID, 'button-confirm')
confirm_button.click()

driver.close()