from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.FIREFOX,
                          command_executor='http://127.0.0.1:4444/wd/hub')
wait = WebDriverWait(driver, 3)

driver.get('http://google.com')
element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.gLFyf.gsfi')))
element.send_keys('Hello World!')

element.send_keys(Keys.ENTER)


