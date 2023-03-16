from time import sleep

import page
from base.base import Base, log


class PageMpAddScore(Base):
    # 点击添加成绩菜单
    def page_click_add_score(self):
        self.base_click(page.mp_add_score)

    # 选择学生
    def page_click_select_student(self, student_name):
        self.web_base_click_element(placeholder_text="请选择", click_text=student_name)

    # 添加成绩
    def page_input_title_name(self, score):
        self.base_input(page.mp_score, score)

    # 点击确认按钮
    def page_click_submit(self):
        sleep(2)
        self.base_click(page.mp_submit_score)

    # 获取发布提示信息
    def page_get_info(self):
        return self.base_get_text(page.mp_alert)

    # 组合添加成绩业务方法
    def page_mp_addScore(self, student_name, score):
        log.info("正在调用添加成绩业务方法，学生姓名: {} 成绩: {}".format(student_name, score))
        self.page_click_add_score()
        self.page_click_select_student(student_name)
        self.page_input_title_name(score)
        self.page_click_submit()
        self.page_get_info()
