import allure
import pytest as pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()

@allure.severity(allure.severity_level.BLOCKER)
@allure.epic("针对业务场景的测试")
@allure.feature("上传课题")
class TestMpTitle:

    # 测试业务方法
    @allure.title("上传课题--预期成功")
    @pytest.mark.parametrize("title_name, degree_text, type_text, source_text, title_abstract,expect_alert", read_yaml("mp_title.yaml")["test_title_sucess"])
    def test_mp_title(self, title_name, degree_text, type_text, source_text, title_abstract, expect_alert, exe_driver_title):
        # 调用登录业务方法
        exe_driver_title.page_mp_title(title_name, degree_text, type_text, source_text, title_abstract)
        try:
            assert expect_alert == exe_driver_title.page_get_info()
        except Exception as e:
            # 输出错误信息
            log.error("断言出错，错误信息: {}".format(e))
            print("错误原因：", e)
            # 截图
            exe_driver_title.base_get_img()
            # 抛出异常
            raise
