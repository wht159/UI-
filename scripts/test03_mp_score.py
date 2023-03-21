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
def Score_fixture():
    db.execute_db(sql["test_score_sql"])
    log.info("执行前置SQL：{}".format(sql["test_score_sql"]))
    yield
    db.execute_db(sql["test_score_sql"])
    log.info("执行前置SQL：{}".format(sql["test_score_sql"]))


@allure.severity(allure.severity_level.BLOCKER)
@allure.epic("针对业务场景的测试")
@allure.feature("添加成绩")
class TestMpScore:
    # 测试业务方法
    @allure.title("添加成绩--预期成功")
    @pytest.mark.parametrize("student, score, expect_alert", read_yaml("mp_score.yaml")["test_add_score_success"])
    def test_mp_score_success(self, student, score, expect_alert, exe_driver, Score_fixture):

        # 获取统一入口类获取对象
        page_in = PageIn(exe_driver)
        # 获取PageMpLogin对象并调用成功登录依赖的方法
        page_in.page_get_pageMpLogin().page_mp_teacher_login()
        # 获取page_get_pageMpScore页面对象
        MpScore = page_in.page_get_pageMpScore()
        # 调用添加成绩业务方法
        MpScore.page_mp_addScore(student, score)
        sleep(1)
        try:
            assert expect_alert == MpScore.page_get_info()
        except Exception as e:
            # 输出错误信息
            log.error("断言出错，错误信息: {}".format(e))
            print("错误原因：", e)
            # 截图
            MpScore.base_get_img()
            # 抛出异常
            raise

    @allure.title("添加成绩--预期失败")
    @pytest.mark.flaky(reruns=5)
    @pytest.mark.parametrize("student, score, expect_alert", read_yaml("mp_score.yaml")["test_add_score_error"])
    def test_mp_score_error(self, student, score, expect_alert, exe_driver):
        # 获取统一入口类获取对象
        page_in = PageIn(exe_driver)
        # 获取PageMpLogin对象并调用成功登录依赖的方法
        page_in.page_get_pageMpLogin().page_mp_teacher_login()
        # 获取page_get_pageMpScore页面对象
        MpScore = page_in.page_get_pageMpScore()
        # 调用添加成绩业务方法
        MpScore.page_mp_addScore(student, score)
        sleep(1)
        try:
            assert expect_alert == MpScore.page_get_info()
        except Exception as e:
            # 输出错误信息
            log.error("断言出错，错误信息: {}".format(e))
            print("错误原因：", e)
            # 截图
            MpScore.base_get_img()
            # 抛出异常
            raise





