from time import sleep

from base.base import Base
import page
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageMpLogin(Base):

    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.mp_username, username)

    # 输入密码
    def page_input_password(self, password):
        self.base_input(page.mp_password, password)

    # 点击登录按钮
    def page_click_login_btn(self):
        self.base_click(page.mp_login_btn)

    # 获取角色封装
    def page_get_role(self):
        return self.base_get_text(page.mp_role)

    # 获取弹窗信息
    def page_get_alert(self):
        return self.base_get_text(page.mp_alert)

    # 获取弹窗信息
    def page_get_form_item_error(self):
        return self.base_get_mult_text(page.mp_form_item_error)

    # 组合 测试脚本层调用
    def page_mp_login(self, username, password):
        log.info("正在调用登录业务方法，用户名: {} 密码: {}".format(username, password))
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_btn()
        sleep(1)

    # 组合 教师登录\成绩输入
    def page_mp_teacher_login(self, username='11111', password='123'):
        log.info("正在调用导师登录业务方法，用户名: {} 密码: {}".format(username, password))

        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_btn()

    # 组合 学生登录\成绩输入
    def page_mp_login_student(self, username='student', password='123'):
        log.info("正在调用学生登录业务方法，用户名: {} 密码: {}".format(username, password))

        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_btn()

    # 管理员登录\成绩输入
    def page_mp_login_admin(self, username='admin', password='admin'):
        log.info("正在调用管理员登录业务方法，用户名: {} 密码: {}".format(username, password))

        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_btn()
