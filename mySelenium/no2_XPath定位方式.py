import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.baidu.com")
# time.sleep(5)
# sousuokuang = driver.find_element("XPATH", '//input[@id="kw"]')
sousuokuang = driver.find_element(By.XPATH, '//input[@id="kw"]')  # 也可以

sousuokuang.send_keys("selenium")  # 输入框中填入 selenium
time.sleep(1)  # 等待1秒
# driver.find_element(By.XPATH, '//input[@value="百度一下"]').click()
driver.find_element(By.XPATH, "//input[@id='su']").click() # 单击搜索框
time.sleep(2) # 等待2秒

