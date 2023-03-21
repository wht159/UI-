import allure
import pytest as pytest

from page.page_in import PageIn
from tools.con_sql import db
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()
sql = read_yaml("mp_sql.yaml")


@pytest.fixture(scope='function')
def Upload_fixture():
    db.execute_db(sql["test_proposal_sql"])
    log.info("执行前置SQL：{}".format(sql["test_proposal_sql"]))
    yield
    db.execute_db(sql["test_proposal_sql"])
    log.info("执行前置SQL：{}".format(sql["test_proposal_sql"]))


@allure.severity(allure.severity_level.BLOCKER)
@allure.epic("针对业务场景的测试")
@allure.feature("上传文件")
class TestMpUpload:
    # 测试业务方法
    @allure.title("上传开题报告--预期成功")
    @pytest.mark.parametrize("url, expect", read_yaml("mp_upload.yaml")["test_upload_proposal"])
    def test_mp_score_success(self, url, expect, exe_driver, Upload_fixture):
        # 获取统一入口类获取对象
        page_in = PageIn(exe_driver)
        # 获取PageMpLogin对象并调用成功登录依赖的方法
        page_in.page_get_pageMpLogin().page_mp_login_student()
        # 获取page_get_pageMpScore页面对象
        MpUpload = page_in.page_get_pageMpUpload()
        # 调用上传业务方法
        MpUpload.page_upload_proposal(url)
        try:
            assert expect == MpUpload.page_get_publish_title()
        except Exception as e:
            # 输出错误信息
            log.error("断言出错，错误信息: {}".format(e))
            print("错误原因：", e)
            # 截图
            MpUpload.base_get_img()
            # 抛出异常
            raise
