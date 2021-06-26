from selenium import webdriver


driver = webdriver.Chrome(executable_path='drivers/chromedriver')
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")
driver.maximize_window()
returning_customer_btn=driver.find_element_by_xpath("//*[@id='input-email']")
returning_customer_btn.click()
email_input= driver.find_element_by_id("input-email")
email_input.clear()
email_input.send_keys(123)

returning_customer_btn=driver.find_element_by_xpath("//*[@id='input-password']")
returning_customer_btn.click()
password_input= driver.find_element_by_id("input-password")
password_input.clear()
password_input.send_keys(345)

returning_customer_btn =driver.find_element_by_xpath("//*[@id='content']/div/div[2]/div/form/input")
returning_customer_btn.click()