from time import sleep

import allure
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


from tools.get_log import GetLog

log = GetLog.get_logger()


class Base:

    # 初始化
    def __init__(self, driver:WebDriver):
        log.info("正在初始化driver：")
        self.driver = driver

    # 查找单个方法封装
    def base_find(self, loc, timeout=30, poll=0.5):
        # :param loc: 格式为列表或元祖，内容: 元素定位信息使用By类
        # :param timeout: 查找元素超时时间，默认30秒
        # :param poll: 查找元素频率默认为0.5
        # :return:元素
        log.info("正在查找元素：{}".format(loc))

        return (WebDriverWait(self.driver,
                              timeout=timeout,
                              poll_frequency=poll).until(lambda x: x.find_element(*loc)))

    # 查找多个方法封装
    def base_find_mult(self, loc, timeout=30, poll=0.5):
        # :param loc: 格式为列表或元祖，内容: 元素定位信息使用By类
        # :param timeout: 查找元素超时时间，默认30秒
        # :param poll: 查找元素频率默认为0.5
        # :return:元素
        log.info("正在查找元素：{}".format(loc))

        return (WebDriverWait(self.driver,
                              timeout=timeout,
                              poll_frequency=poll).until(lambda x: x.find_elements(*loc)))

    # 输入方法封装
    def base_input(self, loc, value):
        # :param loc: 元素的定位信息
        # :param value: 要输入的值

        # 1.获取元素
        el = self.base_find(loc)
        # 2.清空操作
        log.info("正在对: {}元素执行清空操作! ".format(loc))
        el.clear()
        # 3.输入操作
        log.info("正在对: {}元素执行输入:{} 操作!".format(loc, value))
        el.send_keys(value)

    # 点击方法封装

    def base_click(self, loc):
        # param loc: 元素定位信息
        # 获取元素并点击
        log.info("正在对: {} 元素执行点击操作 ".format(loc))
        self.base_find(loc).click()

    # 获取单个元素文本
    def base_get_text(self, loc):
        # param lod: 元素定位信息
        # return: 返回元素的文本值
        log.info("正在对: {}元素获取文本操作!，获取的文本值: {} ".format(loc, self.base_find(loc).text))
        return self.base_find(loc).text

        # 获取多个元素文本
    def base_get_mult_text(self, loc):
        # param loc: 元素定位信息
        # return: 返回元素的文本值
        texts = []
        for i in self.base_find_mult(loc):
            text = i.text
            texts.append(text)
        log.info("正在对: {}元素获取文本操作!，获取的文本值: {} ".format(loc, texts))
        return texts

    # 截图
    def base_get_img(self):
        log.info("断言出错， 正在执行截图操作！")
        allure.attach(self.driver.get_screenshot_as_png(), "错误原因: ", attachment_type=allure.attachment_type.PNG)
        # # 1.调用截图方法
        # self.driver.get_screenshot_as_file('./image/err.png')
        # log.info("断言出错，正在将错误图片写入allure报告！ ")

        # # 2.调用图片写入报告方法
        # self.__base_write_img()

    # # 将图片写入报告方法(私有)
    # def __base_write_img(self):
    #     # 1.获取图片文件流
    #     with open("./image/err.png", "rb") as f:
    #         allure.attach("错误原因: ", f.read(), attachment_type=allure.attachment_type.PNG)

    # 多选框点击操作
    def web_base_click_element(self, placeholder_text, click_text):
        # 1.点击父选框
        loc = By.CSS_SELECTOR, " [placeholder='{}']".format(placeholder_text)
        self.base_click(loc)
        # 2.暂停
        sleep(1)
        # 3.点击包含显示文本的元素
        loc = By.XPATH, "//*[text( )='{}']".format(click_text)
        self.base_click(loc)
    #
    # # 查找弹窗的文本
    # def web_base_find_alter_text(self):
    #     alter = self.driver.switch_to_alert()
    #     return alter.text

