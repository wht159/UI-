from time import sleep

import allure
import pytest as pytest

from page.page_in import PageIn
from tools.con_sql import db
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()
sql = read_yaml("mp_sql.yaml")


@pytest.fixture(scope='function')
def Register_fixture():
    db.execute_db(sql["test_student_register_sql01"])
    db.execute_db(sql["test_student_register_sql02"])
    log.info("执行前置SQL：{}".format(sql["test_student_register_sql01"]))
    log.info("执行前置SQL：{}".format(sql["test_student_register_sql02"]))
    yield
    db.execute_db(sql["test_student_register_sql01"])
    db.execute_db(sql["test_student_register_sql02"])
    log.info("执行前置SQL：{}".format(sql["test_student_register_sql01"]))
    log.info("执行前置SQL：{}".format(sql["test_student_register_sql02"]))


@allure.severity(allure.severity_level.BLOCKER)
@allure.epic("针对业务场景的测试")
@allure.feature("用户注册")
class TestMpRegister:
    # 学生注册业务方法
    @allure.title("注册学生用户--预期成功")
    @pytest.mark.parametrize("username, password, Confirm_Password, name, sno, department,expect_alert",
                             read_yaml("mp_register.yaml")[
                                 "test_register_student_01"])
    def test_student_register_success(self, username, password, Confirm_Password, name, sno, department, exe_driver,
                                      expect_alert,Register_fixture):
        # 通过统一入口类获取PageMpLogin对象
        mpRegister = PageIn(exe_driver).page_get_pageMpRegister()
        # 调用注册业务方法
        mpRegister.page_student_register(username, password, Confirm_Password, name, sno, department)
        # 断言
        try:
            assert expect_alert == mpRegister.page_get_info()
        except Exception as e:
            # 输出错误信息
            log.error("断言出错，错误信息: {}".format(e))
            print("错误原因：", e)
            # 截图
            mpRegister.base_get_img()
            # 抛出异常
            raise

    # 学生注册业务方法失败
    @allure.title("注册学生用户--预期失败")
    @allure.description("两次密码确认不一致")
    @pytest.mark.parametrize("username, password, Confirm_Password, name, sno, department, expect_alert",
                             read_yaml("mp_register.yaml")[
                                 "test_register_student_02"])
    def test_student_register_error(self, username, password, Confirm_Password, name, sno, department, expect_alert,
                                    exe_driver, Register_fixture):
        # 通过统一入口类获取PageMpLogin对象
        mpRegister = PageIn(exe_driver).page_get_pageMpRegister()
        # 调用注册业务方法
        mpRegister.page_student_register(username, password, Confirm_Password, name, sno, department)
        sleep(1)
        # 断言
        try:
            assert expect_alert == mpRegister.page_get_info()
        except Exception as e:
            # 输出错误信息
            log.error("断言出错，错误信息: {}".format(e))
            print("错误原因：", e)
            # 截图
            mpRegister.base_get_img()
            # 抛出异常
            raise

    # 学生注册业务方法失败
    @allure.title("注册学生用户--预期失败")
    @allure.description("没有填写学号信息")
    @pytest.mark.parametrize("username, password, Confirm_Password, name, sno, department, expect_alert",
                             read_yaml("mp_register.yaml")[
                                 "test_register_student_03"])
    def test_student_register_error2(self, username, password, Confirm_Password, name, sno, department, expect_alert,
                                     exe_driver, Register_fixture):
        # 通过统一入口类获取PageMpLogin对象
        mpRegister = PageIn(exe_driver).page_get_pageMpRegister()
        # 调用注册业务方法
        mpRegister.page_student_register(username, password, Confirm_Password, name, sno, department)
        sleep(1)
        # 断言
        try:
            assert expect_alert == mpRegister.page_get_name_info()
        except Exception as e:
            # 输出错误信息
            log.error("断言出错，错误信息: {}".format(e))
            print("错误原因：", e)
            # 截图
            mpRegister.base_get_img()
            # 抛出异常
            raise

    # 导师注册业务方法
    @allure.title("注册导师用户--预期成功")
    @pytest.mark.parametrize("username, password, Confirm_Password, name, tno, department,expect_alert",
                             read_yaml("mp_register.yaml")[
                                 "test_register_teacher_01"])
    def test_mp_teacher_register(self, username, password, Confirm_Password, name, tno, department, exe_driver,
                                 expect_alert, Register_fixture):
        # 通过统一入口类获取PageMpLogin对象
        mpRegister = PageIn(exe_driver).page_get_pageMpRegister()
        # 调用上传业务方法
        mpRegister.page_teacher_register(username, password, Confirm_Password, name, tno, department)
        try:
            assert expect_alert == mpRegister.page_get_info()
        except Exception as e:
            # 输出错误信息
            log.error("断言出错，错误信息: {}".format(e))
            print("错误原因：", e)
            # 截图
            mpRegister.base_get_img()
            # 抛出异常
            raise
