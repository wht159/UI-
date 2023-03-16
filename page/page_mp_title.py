from time import sleep

import page
from base.base import Base, log


class PageMpTitle(Base):
    # 点击上传课题
    def page_click_publish_title(self):
        self.base_click(page.mp_publish_title)

    # 输入课题名称
    def page_input_title_name(self, title_name):
        self.base_input(page.mp_title_name, title_name)

    # 选择课题难度
    def page_click_degree(self, degree_text):
        self.web_base_click_element(placeholder_text="请选择课题难度", click_text=degree_text)

    # 选择课题类型
    def page_click_type(self, type_text):
        self.web_base_click_element(placeholder_text="请选择课题类型", click_text=type_text)

    # 选择课题来源
    def page_click_source(self, source_text):
        self.web_base_click_element(placeholder_text="请选择课题来源", click_text=source_text)

    # 输入课题摘要
    def page_input_abstract(self, title_abstract):
        self.base_input(page.mp_title_abstract, title_abstract)

    # 点击发布课题
    def page_click_submit(self):
        self.base_click(page.mp_submit_title)

    # 获取发布提示信息
    def page_get_info(self):
        return self.base_get_text(page.mp_alert)

    # 组合上传课题业务方法
    def page_mp_title(self, title_name, degree_text, type_text, source_text, title_abstract):
        log.info("正在调用上传课题业务方法，课题名称: {} 课题难度: {} 课题类型: {} 课题来源: {} 课题摘要: {}".format(title_name,
                                                                                    degree_text,
                                                                                    type_text,
                                                                                    source_text,
                                                                                    title_abstract))
        self.page_click_publish_title()
        self.page_input_title_name(title_name)
        self.page_click_degree(degree_text)
        self.page_click_type(type_text)
        self.page_click_source(source_text)
        self.page_input_abstract(title_abstract)
        self.page_click_submit()
        self.page_get_info()
