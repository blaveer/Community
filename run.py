from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

accounts=["420111001010001",
              "420111001010002",
              "420111001010003",
              "420111001010004",
              "420111001010005",
              "420111001010006"]
for account in accounts:
    driver = webdriver.Chrome()
    driver.get("http://10.104.26.51/geoshgl/") #10.105.42.33
    time.sleep(2)
    driver.find_element_by_name("user").clear()
    driver.find_element_by_name("user").send_keys(account)
    driver.find_element_by_name("pwd").clear()
    driver.find_element_by_name("pwd").send_keys("123")
    driver.find_element_by_name("pwd").send_keys(Keys.ENTER)
    print("登陆成功")
    time.sleep(5)
    driver.find_element_by_id("menu_465").click()
    print("点击信息采集按钮")
    time.sleep(3)
    #iframe=driver.find_element_by_id("MFrame")
    driver.switch_to.frame("MFrame")
    print("转换Frame成功")
    time.sleep(5)
    driver.find_element_by_id("ycj").click()
    #driver.find_element_by_xpath("//div[@class='p_gk_left_info_box']/div[@class='p_tab_border']/div[@class='p_tab_box']/div[@id='ycj']").click()
    print("点击已采集按钮")
    time.sleep(5)
    #ycj=driver.find_element_by_class_name("yxswcjtr")
    ycj=driver.find_elements_by_class_name("yxswcjtr")
    print("即将开始遍历栋")
    for ycjOne in ycj:
        ycjOne.click()
        time.sleep(1)
        print("点击单元户成功")
        time.sleep(2)
        driver.switch_to.frame("iframe")
        ul=driver.find_element_by_xpath("//*[@class='xlyt-btnbox']/ul")
        lis=ul.find_elements_by_xpath("li")
        #print(len(lis))
        lis[-1].click()
        print("点击分户图成功")
        time.sleep(3)
        options_select=driver.find_element_by_id("ComboLdDyNo") #单元号
        options=Select(options_select).options
        print("单元号的数量是"+str(len(options)))
        for option in options:
            option.click()
            time.sleep(2)
            print("点击单元号成功")
            # floors=driver.find_elements_by_class_name("xfht-floor")   #这个是分层的
            # time.sleep(1)
            # for floor in floors:
            rooms=driver.find_elements_by_class_name("xhroom-xbox")
            time.sleep(1)
            roomNum=len(rooms)
            room=0
            print("房间的数量是："+str(len(rooms)))
            #for room in rooms:
            while room<roomNum:
                rooms[room].click()
                time.sleep(3)
                #下面这部分先注释，不执行
                driver.switch_to.default_content()
                driver.switch_to.frame("lhgfrm_FWDialog")
                time.sleep(2)
                driver.find_element_by_id("btnRoomFormEdit").click()
                areaOfConstruction=float(driver.find_element_by_id("txtJzArea").get_attribute("value"))
                areaOfDwell=float(driver.find_element_by_id("txtJzMJ").get_attribute("value"))
                if areaOfConstruction>0:
                    if areaOfDwell>0:
                        print("无需该更面积")
                    else:
                        driver.find_element_by_id("txtJzMJ").send_keys(str(areaOfConstruction))
                        print("改改了居住面积")
                else:
                    if areaOfDwell>0:
                        driver.find_element_by_id("txtJzArea").send_keys(str(areaOfDwell))
                        print("更改了建筑面积")
                    else:
                        driver.find_element_by_id("txtJzMJ").send_keys("30.0")
                        driver.find_element_by_id("txtJzArea").send_keys("30.0")
                        print("俩都改为30了")
                options_select_capsule = driver.find_element_by_id("sltjnf")  # 胶囊房
                options_select_capsule_items = Select(options_select_capsule).options
                options_select_capsule_items[1].click()
                driver.find_element_by_id("btnxRoomSave").click()
                time.sleep(3)
                #TODO 叉掉保存后的那个按钮
                time.sleep(10)  ##
                driver.switch_to.default_content()
                driver.find_element_by_id("lhgdg_xbtn_FWDialog").click()
                #driver.switch_to.default_content()
                driver.switch_to.frame("MFrame")
                driver.switch_to.frame("iframe")
                time.sleep(3)
                print("结束了一个房间的任务")
                #结束了一个房间的任务
                room=room+1
                rooms = driver.find_elements_by_class_name("xhroom-xbox")
                time.sleep(1)

            #结束了一片的任务
        time.sleep(3)
        driver.switch_to.default_content()
        driver.switch_to.frame("MFrame")
    print("完成一个用户的")
    driver.quit()
print("全部账号扫描过一次了")




