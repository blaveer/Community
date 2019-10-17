import selenium as webdriver
import time

if __name__ == '__main__':
    accounts=["420111001010",
              "420111001010001",
              "420111001010002",
              "420111001010003",
              "420111001010004",
              "420111001010005",
              "420111001010006"]
    for account in accounts:
        driver = webdriver.Chrome()
        driver.get("http://10.104.26.51/geoshgl/")
        time.sleep(2)
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(account)
        driver.find_element_by_name("pwd").clear()
        driver.find_element_by_name("pwd").send_keys("123")
        driver.find_element_by_id("btnLogin").click()
        time.sleep(10)






