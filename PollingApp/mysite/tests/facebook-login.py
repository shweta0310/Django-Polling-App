from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome('/home/shweta/chromedriver_linux64/chromedriver')
driver.get ("https://www.facebook.com")

driver.find_element_by_id("email").send_keys("shwetaiyerbaroda@gmail.com")
driver.find_element_by_id("pass").send_keys("shrriyer")
driver.find_element_by_name("login").click()

WebDriverWait(driver, 1).until(EC.title_contains("home"))
