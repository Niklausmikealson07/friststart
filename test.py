from selenium import webdriver

driver=webdriver.Chrome(r"D:\chromedriver.exe")
driver.maximize_window()
driver.get('https://meesho.com/')