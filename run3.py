from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import time
import random

if __name__ == "__main__":

    accounts = [

                "420111001010005",]
    for account in accounts:
        base=random.randint(60,75)

        driver = webdriver.Chrome()
        driver.get("http://10.104.26.51/geoshgl/")  # 10.105.42.33
        time.sleep(2)
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(account)
        driver.find_element_by_name("pwd").clear()
        driver.find_element_by_name("pwd").send_keys("123")
        driver.find_element_by_name("pwd").send_keys(Keys.ENTER)
        print("登陆成功:账号" + account)
        #time.sleep(6)
        try:
            menu_info_get = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id("menu_465"))
        except:
            print("请检查网络，在寻找信息采集按钮时候出错")
        else:
            menu_info_get.click()
            time.sleep(3)
            print("   点击信息采集按钮:已经入信息采集界面")
            driver.switch_to.frame("MFrame")
            # try:
            #     WebDriverWait(driver, 20).until(lambda driver:driver.switch_to.frame("MFrame"))
            # except:
            #     print("请检查网络:在转换Frame时候出错")
            # else:
            print("   转换Frame成功：进入到单元号小区所在Frame")

            ycj_button=driver.find_element_by_id("ycj")
            # try:
            #     ycj_button = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id("ycj"))
            # except:
            #     print("请检查网络：在点击已采集按钮的地方出错")
            # else:
            time.sleep(10)
            try:
                ycj_button.click()
            except:
                print("点击已采集按钮报错")
                continue
            print("   点击已采集按钮：再次确认进入到该Frame")
            # time.sleep(5)
            try:
                ycj = WebDriverWait(driver, 20).until(lambda driver: driver.find_elements_by_class_name("yxswcjtr"))
            except:
                print("请检查网络：在获取已采集列表时候出错")
            else:
                print("   即将开始遍历栋小区")
                counter_xiaoqu = 1
                for ycjOne in ycj:
                    try:
                        ycjOne.click()
                        # time.sleep(1)
                        print("   点击单元户成功:第" + str(counter_xiaoqu) + "个小区")
                        time.sleep(2)
                        driver.switch_to.frame("iframe")

                        time.sleep(1)
                        ul = driver.find_element_by_xpath("//*[@class='xlyt-btnbox']/ul")
                        lis = ul.find_elements_by_xpath("li")
                        # print(len(lis))
                        lis[-1].click()
                        print("   点击分户图成功:进入到小区界面")
                        # time.sleep(3)
                        try:
                            options_select = WebDriverWait(driver, 20).until(
                                lambda driver: driver.find_element_by_id("ComboLdDyNo"))  # 单元号
                        except:
                            print("请检查网络：在获取单元号列表是出错")
                        else:
                            options = Select(options_select).options
                            print("   第" + str(counter_xiaoqu) + "个小区的单元号的数量是" + str(len(options)))
                            counter_danyuanhao = 1
                            for option in options:
                                option.click()
                                # time.sleep(2)
                                print("      点击第" + str(counter_xiaoqu) + "个小区的单元号成功:第" + str(
                                    counter_danyuanhao) + "个单元号")
                                try:
                                    floor = WebDriverWait(driver, 20).until(
                                        lambda driver: driver.find_elements_by_class_name("xfht-floor"))
                                except:
                                    print("请检查网络：在获取该单元层数时候出错")
                                else:
                                    # time.sleep(1)
                                    floorNum = len(floor)
                                    try:
                                        rooms = WebDriverWait(driver, 20).until(
                                            lambda driver: driver.find_elements_by_class_name("xhroom-xbox"))
                                    except:
                                        print("请检查网络：获取该单元的全部房间时候出错")
                                    else:
                                        # time.sleep(1)
                                        num_of_each_floor = len(rooms) / floorNum
                                        time_left_click = int(num_of_each_floor / 4)
                                        print("要按左键" + str(time_left_click))
                                        roomNum = len(rooms)
                                        room = 0
                                        print("      第" + str(counter_xiaoqu) + "个小区的第" + str(
                                            counter_danyuanhao) + "单元号下房间的数量是：" + str(
                                            len(rooms)))
                                        # for room in rooms:
                                        counter_right_time = 0
                                        counter_room = 1
                                        while room < roomNum:
                                            IsPass = random.randint(0, 100)
                                            if IsPass < base:
                                                try:
                                                    # region 房间点击部分
                                                    rooms[room].click()
                                                    # time.sleep(3)
                                                    print(
                                                        "         正在遍历第" + str(counter_xiaoqu) + "个小区的第" + str(
                                                            counter_danyuanhao) + "单元号下的第" + str(
                                                            room + 1) + "个房间")
                                                    driver.switch_to.default_content()
                                                    driver.switch_to.frame("lhgfrm_FWDialog")
                                                    # region 更改具体房间的代码
                                                    time.sleep(2)
                                                    driver.find_element_by_id("btnRoomFormEdit").click()
                                                    print("            点击编辑房间按钮成功")
                                                    areaOfConstruction = float(
                                                        driver.find_element_by_id("txtJzArea").get_attribute(
                                                            "value"))
                                                    areaOfDwell = float(
                                                        driver.find_element_by_id("txtJzMJ").get_attribute("value"))
                                                    if areaOfConstruction > 0:
                                                        if areaOfDwell > 0:
                                                            print("               无需该更面积")
                                                        else:
                                                            driver.find_element_by_id("txtJzMJ").send_keys(
                                                                str(areaOfConstruction))
                                                            print("               改改了居住面积")
                                                    else:
                                                        if areaOfDwell > 0:
                                                            driver.find_element_by_id("txtJzArea").send_keys(
                                                                str(areaOfDwell))
                                                            print("               更改了建筑面积")
                                                        else:
                                                            driver.find_element_by_id("txtJzMJ").send_keys("30.0")
                                                            driver.find_element_by_id("txtJzArea").send_keys("30.0")
                                                            print("               俩都改为30了")
                                                    options_select_capsule = driver.find_element_by_id(
                                                        "sltjnf")  # 胶囊房
                                                    options_select_capsule_items = Select(
                                                        options_select_capsule).options
                                                    options_select_capsule_items[1].click()
                                                    print("               更改为胶囊房成功")
                                                    driver.find_element_by_id("btnxRoomSave").click()
                                                    time.sleep(2)
                                                    # TODO 叉掉保存后的那个按钮
                                                    time.sleep(10)  ##
                                                    # endregion
                                                    driver.switch_to.default_content()
                                                    driver.find_element_by_id("lhgdg_xbtn_FWDialog").click()
                                                    # driver.switch_to.default_content()
                                                    # endregion
                                                except:
                                                    print("         第" + str(counter_xiaoqu) + "个小区的第" + str(
                                                        counter_danyuanhao) + "单元号的第" + str(
                                                        room + 1) + "个房间出错")
                                                finally:
                                                    driver.switch_to.frame("MFrame")
                                                    driver.switch_to.frame("iframe")
                                                    time.sleep(3)
                                                    # print("结束了一个房间的任务")
                                                    print(
                                                        "         第" + str(counter_xiaoqu) + "个小区的第" + str(
                                                            counter_danyuanhao) + "单元号的第" + str(
                                                            room + 1) + "个房间遍历完成")
                                                    # 结束了一个房间的任务
                                                    print(counter_room)
                                                    if num_of_each_floor > 4:
                                                        if (int(counter_room)) % 4 == 0:
                                                            right = driver.find_elements_by_class_name("fht-scroll")
                                                            right[1].click()
                                                            time.sleep(1)
                                                            counter_right_time = counter_right_time + 1
                                                        # if counter_right_time == time_left_click:
                                                        if counter_room % num_of_each_floor == 0:
                                                            for counter_left_time in range(0, counter_right_time):
                                                                left = driver.find_elements_by_class_name("fht-scroll")
                                                                time.sleep(1)
                                                                left[0].click()
                                                                counter_room = 0
                                                    room = room + 1
                                                    counter_room = counter_room + 1
                                                    rooms = driver.find_elements_by_class_name("xhroom-xbox")
                                                    time.sleep(1)
                                            else:
                                                print("跳过了一个房间")
                                                print(counter_room)
                                                if num_of_each_floor > 4:
                                                    if (int(counter_room)) % 4 == 0:
                                                        right = driver.find_elements_by_class_name("fht-scroll")
                                                        right[1].click()
                                                        time.sleep(1)
                                                        counter_right_time = counter_right_time + 1
                                                    # if counter_right_time == time_left_click:
                                                    if counter_room % num_of_each_floor == 0:
                                                        for counter_left_time in range(0, counter_right_time):
                                                            left = driver.find_elements_by_class_name("fht-scroll")
                                                            time.sleep(1)
                                                            left[0].click()
                                                            counter_room = 0
                                                room = room + 1
                                                counter_room = counter_room + 1
                                                rooms = driver.find_elements_by_class_name("xhroom-xbox")
                                                time.sleep(1)

                                        print("      第" + str(counter_xiaoqu) + "个小区的第" + str(
                                            counter_danyuanhao) + "个单元号遍历完成")
                                        counter_danyuanhao = counter_danyuanhao + 1
                                        # 结束了一片的任务
                        print("用户(" + account + ")下第" + str(counter_xiaoqu) + "个小区遍历完成")

                        time.sleep(3)
                        driver.switch_to.default_content()
                        driver.switch_to.frame("MFrame")
                        counter_xiaoqu = counter_xiaoqu + 1
                    except:
                        print("在执行该小区时候出错")
                        driver.switch_to.default_content()
                        driver.switch_to.frame("MFrame")
                        counter_xiaoqu=counter_xiaoqu+1
                        continue

        print("用户(" + account + ")已全部遍历完成")
        driver.quit()
    print("全部账号扫描过一次了")



