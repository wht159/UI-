import allure
import pytest as pytest
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


@allure.severity(allure.severity_level.BLOCKER)
@allure.epic("针对业务场景的测试")
@allure.feature("添加成绩")
class TestMpScore:
    # 测试业务方法
    @allure.title("添加成绩--预期成功")
    @pytest.mark.parametrize("student, score, expect_alert", read_yaml("mp_score.yaml")["test_add_score_success"])
    def test_mp_score_success(self, student, score, expect_alert, exe_driver_score):
        # 调用登录业务方法
        exe_driver_score.page_mp_addScore(student, score)
        try:
            assert expect_alert == exe_driver_score.page_get_info()
        except Exception as e:
            # 输出错误信息
            log.error("断言出错，错误信息: {}".format(e))
            print("错误原因：", e)
            # 截图
            exe_driver_score.base_get_img()
            # 抛出异常
            raise

    @allure.title("添加成绩--预期失败")
    @pytest.mark.parametrize("student, score, expect_alert", read_yaml("mp_score.yaml")["test_add_score_error"])
    def test_mp_score_error(self, student, score, expect_alert, exe_driver_score):
        # 调用登录业务方法
        exe_driver_score.page_mp_addScore(student, score)
        try:
            assert expect_alert == exe_driver_score.page_get_info()
        except Exception as e:
            # 输出错误信息
            log.error("断言出错，错误信息: {}".format(e))
            print("错误原因：", e)
            # 截图
            exe_driver_score.base_get_img()
            # 抛出异常
            raise





