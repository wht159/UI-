import allure
import pytest as pytest

from page.page_in import PageIn
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


@allure.severity(allure.severity_level.BLOCKER)
@allure.epic("针对业务场景的测试")
@allure.feature("用户登录")
class TestMpLogin:

    # 测试业务方法
    @allure.title("用户登录--预期成功")
    @pytest.mark.parametrize("username, password, expect_role", read_yaml("mp_login.yaml")["test_login_sucess"])
    def test_mp_login_sucess(self, username, password, expect_role, exe_driver):
        # 调用登录业务方法
        page_in = PageIn(exe_driver)
        mp = page_in.page_get_pageMpLogin()
        mp.page_mp_login(username, password)

        print(mp.page_get_alert())
        try:
            assert expect_role == mp.page_get_role()
        except Exception as e:
            # 输出错误信息
            log.error("断言出错，错误信息: {}".format(e))
            print("错误原因：", e)
            # 截图
            exe_driver.base_get_img()
            # 抛出异常
            raise

    @allure.title("用户登录--预期失败--用例一")
    @pytest.mark.parametrize("username, password, expect_alert", read_yaml("mp_login.yaml")["test_login_error_1"])
    def test_mp_login_error_1(self, username, password, expect_alert, exe_driver):
        # 调用登录业务方法
        page_in = PageIn(exe_driver)
        mp = page_in.page_get_pageMpLogin()
        mp.page_mp_login(username, password)
        try:
            assert expect_alert == mp.page_get_alert()
        except Exception as e:
            # 输出错误信息
            log.error("断言出错，错误信息: {}".format(e))
            print("错误原因：", e)
            # 截图
            mp.base_get_img()
            # 抛出异常
            raise

    @allure.title("用户登录--预期失败--用例二")
    @pytest.mark.parametrize("username, password, expect_alert", read_yaml("mp_login.yaml")["test_login_error_2"])
    def test_mp_login_error_2(self, username, password, expect_alert, exe_driver):
        # 调用登录业务方法
        page_in = PageIn(exe_driver)
        mp = page_in.page_get_pageMpLogin()
        mp.page_mp_login(username, password)
        try:
            assert expect_alert == mp.page_get_form_item_error()
        except Exception as e:
            # 输出错误信息
            log.error("断言出错，错误信息: {}".format(e))
            print("错误原因：", e)
            # 截图
            mp.base_get_img()
            # 抛出异常
            raise
