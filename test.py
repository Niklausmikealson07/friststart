from selenium import webdriver

driver=webdriver.Chrome(r"D:\chromedriver.exe")
driver.maximize_window()
driver.get('https://meesho.com/')
from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://opensource-demo.orangehrmlive.com')
driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys('admin')
driver.find_element_by_css_selector("input[id='txtPassword']").send_keys('admin123')
driver.find_element_by_css_selector("input[value='LOGIN']").click()
driver.find_element_by_xpath('//*[@id="welcome"]').click()
time.sleep(3)
driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()
