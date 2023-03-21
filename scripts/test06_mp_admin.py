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
def Admin_fixture():
    db.execute_db(sql["test_select_teacher_sql"])
    log.info("执行前置SQL：{}".format(sql["test_select_teacher_sql"]))
    yield
    db.execute_db(sql["test_select_teacher_sql"])
    log.info("执行前置SQL：{}".format(sql["test_select_teacher_sql"]))


@allure.severity(allure.severity_level.BLOCKER)
@allure.epic("针对业务场景的测试")
@allure.feature("管理员业务方法")
class TestMpAdmin:
    # 选择指导老师业务
    @allure.title("选择指导老师--预期成功")
    @pytest.mark.parametrize("sno, teacher_name, expect_result", read_yaml("mp_admin.yaml")["test_select_teacher"])
    def test_mp_student_register(self, sno, teacher_name, expect_result, exe_driver, Admin_fixture):
        # 获取统一入口类获取对象
        page_in = PageIn(exe_driver)
        # 获取PageMpLogin对象并调用成功登录依赖的方法
        page_in.page_get_pageMpLogin().page_mp_login_admin()
        # 获取page_get_pageMpScore页面对象
        admin = page_in.page_get_pageMpAdmin()
        # 更改前令该用户记录为空
        # 调用上传业务方法
        admin.page_select_teacher(sno, teacher_name)

        try:
            assert expect_result == admin.page_get_select_teacher_result()
        except Exception as e:
            # 输出错误信息
            log.error("断言出错，错误信息: {}".format(e))
            print("错误原因：", e)
            # 截图
            admin.base_get_img()
            # 抛出异常
            raise
