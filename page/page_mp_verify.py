from time import sleep

from base.base import Base
import page
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageVerify(Base):
    # 点击审核毕业论文
    def page_click_verify_manage(self):
        self.base_click(page.mp_click_verify_manager)

    # 点击查重按钮
    def page_click_check_paper(self):
        self.base_click(page.mp_click_check_paper)

    # 获取查重信息
    def page_get_check_info(self):
        return self.base_get_text(page.mp_check_info)

    # 点击审核按钮
    def page_click_verify_button(self):
        self.base_click(page.mp_click_verify_paper)

    # 点击审核通过
    def page_click_verify_success(self):
        self.base_js_click_element(page.mp_verify_success)

    # 点击审核不通过
    def page_click_verify_fail(self):
        self.base_js_click_element(page.mp_verify_fail)

    # 输入审核意见
    def page_input_comment(self, comment):
        self.base_input(page.mp_input_comment, comment)

    # 点击提交
    def page_click_submit(self):
        self.base_click(page.mp_verify_submit)

    # 获取发布提示信息
    def page_get_info(self):
        return self.base_get_text(page.mp_alert)

    # 查重论文组合业务
    def page_check_paper(self):
        self.page_click_verify_manage()
        self.page_click_check_paper()

    # 审核论文通过组合业务
    def page_verify_paper(self, comment):
        self.page_click_verify_manage()
        self.page_click_verify_button()
        self.page_click_verify_success()
        self.page_input_comment(comment)
        sleep(3)
        self.page_click_submit()

    # 审核论文不通过组合业务
    def page_verify_fail(self, comment):
        self.page_click_verify_manage()
        self.page_click_verify_button()
        self.page_click_verify_fail()
        self.page_input_comment(comment)
        sleep(3)
        self.page_click_submit()


