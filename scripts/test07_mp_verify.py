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
def verify_fixture():
    db.execute_db(sql["test_verify_paper_sql"])
    log.info("执行前置SQL：{}".format(sql["test_verify_paper_sql"]))
    yield
    db.execute_db(sql["test_verify_paper_sql"])
    log.info("执行前置SQL：{}".format(sql["test_verify_paper_sql"]))


@allure.severity(allure.severity_level.BLOCKER)
@allure.epic("针对业务场景的测试")
@allure.feature("导师审核论文业务方法")
class TestMpVerify:
    @allure.title("查重毕业论文--预期成功")
    def test_mp_check_paper(self, exe_driver):
        page_in = PageIn(exe_driver)
        page_in.page_get_pageMpLogin().page_mp_teacher_login()
        check = page_in.page_get_pageMpVerify()
        check.page_check_paper()
        sleep(1)
        try:
            assert "0.71" == check.page_get_check_info()
        except Exception as e:
            # 输出错误信息
            log.error("断言出错，错误信息: {}".format(e))
            print("错误原因：", e)
            # 截图
            check.base_get_img()
            # 抛出异常
            raise

    @allure.title("审核通过毕业论文--预期成功")
    @pytest.mark.parametrize("comment, expect_alert", read_yaml("mp_verify.yaml")["test_verify_paper_success"])
    def test_mp_verify_paper_success(self, exe_driver, comment, expect_alert, verify_fixture):
        page_in = PageIn(exe_driver)
        page_in.page_get_pageMpLogin().page_mp_teacher_login()
        verify = page_in.page_get_pageMpVerify()
        verify.page_verify_paper(comment)
        sleep(1)
        try:
            assert expect_alert == verify.page_get_info()
        except Exception as e:
            # 输出错误信息
            log.error("断言出错，错误信息: {}".format(e))
            print("错误原因：", e)
            # 截图
            verify.base_get_img()
            # 抛出异常
            raise

    @allure.title("审核不通过毕业论文--预期成功")
    @pytest.mark.parametrize("comment, expect_alert", read_yaml("mp_verify.yaml")["test_verify_paper_fail"])
    def test_mp_verify_paper_fail(self, exe_driver, comment, expect_alert, verify_fixture):
        page_in = PageIn(exe_driver)
        page_in.page_get_pageMpLogin().page_mp_teacher_login()
        verify = page_in.page_get_pageMpVerify()
        verify.page_verify_fail(comment)
        sleep(1)
        try:
            assert expect_alert == verify.page_get_info()
        except Exception as e:
            # 输出错误信息
            log.error("断言出错，错误信息: {}".format(e))
            print("错误原因：", e)
            # 截图
            verify.base_get_img()
            # 抛出异常
            raise
