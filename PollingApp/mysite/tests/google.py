# from selenium import webdriver
#
# driver = webdriver.Chrome('/home/shweta/chromedriver_linux64/chromedriver')
#
# driver.get("https://google.com")
#
# driver.find_element_by_name("q").send_keys("Selenium")


from selenium import webdriver

driver = webdriver.Chrome('/home/shweta/chromedriver_linux64/chromedriver')

driver.get("http://127.0.0.1:8000/en-gb/accounts/login/")

driver.find_element_by_id("id_login-username").send_keys("shwetahiyer@gmail.com")
driver.find_element_by_id("id_login-password").send_keys("shwetaiyer")

# driver.find_element_by_link_text("Log In").click()

driver.find_element_by_name("login_submit").submit()
