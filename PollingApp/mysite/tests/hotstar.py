from selenium import webdriver

driver = webdriver.Chrome('/home/shweta/chromedriver_linux64/chromedriver')

driver.get("https://www.hotstar.com")
driver.maximize_window()
driver.find_element_by_partial_link_text('Premium').click()