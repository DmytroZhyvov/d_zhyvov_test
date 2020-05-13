from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from Homework_9.skyscanner.locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
wait = WebDriverWait(driver, 4)


# open a Home page
driver.get('https://www.skyscanner.com.ua')

# input a value into destination field for a dropdowm to be displayed
wait.until(EC.element_to_be_clickable(DEST_INP)).send_keys('Cт')

# select the first option from destination dropdown
wait.until(EC.element_to_be_clickable(DEST_DRDOWN_VAL_0)).click()

# click on departure field to open a calendar
wait.until(EC.element_to_be_clickable(DEP_DATE_INPUT)).click()

# click on a month dropdown
select_element = driver.find_element(By.CSS_SELECTOR, DEP_MONTH_DRDOWN)
select_object = Select(select_element)
select_element.click()

# select a month option
select_object.select_by_visible_text("вересень 2020")

# get a calendar for a departure date
cal = driver.find_element(By.CSS_SELECTOR, DEP_CALENDAR)

# select a departure date
departure_date = cal.find_elements(By.TAG_NAME, 'tr')[5].find_elements(By.TAG_NAME, 'td')[2]
departure_date.click()

# click on return field to open a calendar
wait.until(EC.element_to_be_clickable(RET_DATE_INPUT)).click()

# click on a month dropdown
select_element = driver.find_element(By.CSS_SELECTOR, RET_MONTH_DRDOWN)
select_object = Select(select_element)
select_element.click()

# select a month option
select_object.select_by_visible_text("жовтень 2020")

# get a calendar for a return date
cal2 = driver.find_element(By.CSS_SELECTOR, RET_CALENDAR)

# select a return date
return_date = cal2.find_elements(By.TAG_NAME, 'tr')[3].find_elements(By.TAG_NAME, 'td')[2]
return_date.click()

# check the direct fly checkbox
driver.find_element(By.CSS_SELECTOR, DIR_FLY_CHBOX).click()

# click on "Пошук Рейсів" button
driver.find_element(By.CSS_SELECTOR, FIND_FLY_BTN).click()

# move departure start slider
dep_lt_slider = wait.until(EC.presence_of_element_located((By.XPATH, DEP_LFT_SLIDER)))
move = ActionChains(driver)
move.click_and_hold(dep_lt_slider).move_by_offset(160, 0).release().perform()

# move departure right slider
dep_rt_slider = wait.until(EC.presence_of_element_located((By.XPATH, DEP_RHT_SLIDER)))
move = ActionChains(driver)
move.click_and_hold(dep_rt_slider).move_by_offset(-30, 0).release().perform()

# move return start slider
ret_lt_slider = wait.until(EC.presence_of_element_located((By.XPATH, RET_LFT_SLIDER)))
move = ActionChains(driver)
move.click_and_hold(ret_lt_slider).move_by_offset(100, 0).release().perform()

# move return right slider
ret_rt_slider = wait.until(EC.presence_of_element_located((By.XPATH, RET_RHT_SLIDER)))
move = ActionChains(driver)
move.click_and_hold(ret_rt_slider).move_by_offset(-80, 0).release().perform()

print('Finished')

