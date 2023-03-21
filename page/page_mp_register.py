from time import sleep

from base.base import Base, log
import page
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageMpRegister(Base):
    # 点击学生注册按钮
    def page_click_student_register_button(self):
        self.base_click(page.mp_student_register_button)

    # 点击教师注册按钮
    def page_click_teacher_register_button(self):
        self.base_click(page.mp_teacher_register_button)

    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.mp_register_username, username)

    # 输入密码
    def page_input_password(self, password):
        self.base_input(page.mp_register_password, password)

    # 输入确认密码
    def page_input_confirm_password(self, Confirm_Password):
        self.base_input(page.mp_confirm_password, Confirm_Password)

    # 输入姓名
    def page_input_name(self, name):
        self.base_input(page.mp_register_name, name)

    # 输入学号
    def page_input_sno(self, sno):
        self.base_input(page.mp_register_sno, sno)

    # 输入工号
    def page_input_tno(self, tno):
        self.base_input(page.mp_register_tno, tno)

    # 输入所在院系
    def page_input_confirm_department(self, department):
        self.base_input(page.mp_register_department, department)

    # 点击学生注册按钮
    def page_click_register_button(self):
        self.base_click(page.mp_confirm_register_button)

    # 获取注册结果弹窗信息
    def page_get_info(self):
        return self.base_get_text(page.mp_alert)

    # 获取注册结果弹窗信息
    def page_get_name_info(self):
        return self.base_get_text(page.mp_sno_alter)

    # 学生注册组合业务
    def page_student_register(self, username, password, Confirm_Password, name, sno, department):
        self.page_click_student_register_button()
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_input_confirm_password(Confirm_Password)
        self.page_input_name(name)
        self.page_input_sno(sno)
        self.page_input_confirm_department(department)
        self.page_click_register_button()

    # 导师注册组合业务
    def page_teacher_register(self, username, password, Confirm_Password, name, tno, department):
        self.page_click_student_register_button()
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_input_confirm_password(Confirm_Password)
        self.page_input_name(name)
        self.page_input_sno(tno)
        self.page_input_confirm_department(department)
        self.page_click_register_button()