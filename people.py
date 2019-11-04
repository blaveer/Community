from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import time

if __name__ == "__main__":
    driver = webdriver.Ie()
    driver.get("http://10.104.26.51/geoshgl/")  # 10.105.42.33
    time.sleep(5)
    account="420111001010003"
    driver.find_element_by_name("user").clear()
    driver.find_element_by_name("user").send_keys(account)
    driver.find_element_by_name("pwd").clear()
    driver.find_element_by_name("pwd").send_keys("123")
    driver.find_element_by_name("pwd").send_keys(Keys.ENTER)
    print("登陆成功:账号" + account)