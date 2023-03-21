from time import sleep

from selenium.webdriver.common.by import By

from base.base import Base
import page
from tools.get_log import GetLog
import win32com.client

log = GetLog.get_logger()


class PageUpAdmin(Base):
    # 点击学生管理
    def page_click_student_manager(self):
        self.base_click(page.mp_student_manager)
        sleep(3)

    # 输入学号
    def page_input_sno(self, sno):
        self.base_input(page.mp_input_sno, sno)

    # 点击搜索学号
    def page_click_select_sno(self):
        self.base_click(page.mp_select_sno_button)

    # 点击选择指导老师
    def page_clicl_select_Teacher_item(self):
        self.base_click(page.mp_select_Teacher_button)

    # 选择指导老师
    def page_click_select_Teacher(self, teacher_name):
        self.web_base_click_element(placeholder_text="请选择老师", click_text=teacher_name)

    # 点击确认
    def page_click_confirm(self):
        self.base_click(page.mp_confirm_select_Teacher_button)

    # 获取选择结果
    def page_get_select_teacher_result(self):
        return self.base_get_text(page.mp_select_teacher_result)

    # 组合选择导师业务
    def page_select_teacher(self, sno, teacher_name):
        self.page_click_student_manager()
        self.page_input_sno(sno)
        self.page_click_select_sno()
        self.page_clicl_select_Teacher_item()
        self.page_click_select_Teacher(teacher_name)
        self.page_click_confirm()
