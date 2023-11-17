from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
element = driver.find_element(By.ID, "kw").accessible_name

# 打印对象上的属性和方法
print(dir(element))
print(dir(driver.find_element(By.ID, "kw")))
# print(vars(element))

# print(dir(element))
