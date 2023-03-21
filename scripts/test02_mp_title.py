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
def Title_fixture():
    db.execute_db(sql["test_title_sql"])
    log.info("执行前置SQL：{}".format(sql["test_title_sql"]))
    yield
    db.execute_db(sql["test_title_sql"])
    log.info("执行前置SQL：{}".format(sql["test_title_sql"]))


@allure.severity(allure.severity_level.BLOCKER)
@allure.epic("针对业务场景的测试")
@allure.feature("上传课题")
class TestMpTitle:

    # 测试业务方法
    @allure.title("上传课题--预期成功")
    @pytest.mark.parametrize("title_name, degree_text, type_text, source_text, title_abstract,expect_alert",
                             read_yaml("mp_title.yaml")["test_title_success"])
    def test_mp_title(self, title_name, degree_text, type_text, source_text, title_abstract, expect_alert, exe_driver, Title_fixture):
        # 获取统一入口类获取对象
        page_in = PageIn(exe_driver)
        # 获取PageMpLogin对象并调用成功登录依赖的方法
        page_in.page_get_pageMpLogin().page_mp_teacher_login()
        # 获取PageMpTitle页面对象
        MpTitle = page_in.page_get_pageMpTitle()
        # 调用业务方法
        MpTitle.page_mp_title(title_name, degree_text, type_text, source_text, title_abstract)
        sleep(1)
        try:
            assert expect_alert == MpTitle.page_get_info()
        except Exception as e:
            # 输出错误信息
            log.error("断言出错，错误信息: {}".format(e))
            print("错误原因：", e)
            # 截图
            MpTitle.base_get_img()
            # 抛出异常
            raise
