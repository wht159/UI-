from time import sleep

from base.base import Base
import page
from tools.get_log import GetLog
import win32com.client

log = GetLog.get_logger()


class PageUpLoad(Base):
    # 点击上传页面
    def page_click_publish_begin(self):
        self.base_click(page.mp_publish_begin)

    # 点击上传按钮
    def page_click_publish_button(self, url):
        self.base_click(page.mp_publish_button)
        sleep(2)  # 等待上传选择文件对话框打开
        shell = win32com.client.Dispatch("WScript.Shell")

        # 输入文件路径，最后的'\n'，表示回车确定，也可能时 '\r' 或者 '\r\n'
        shell.Sendkeys(r"{}".format(url) + '\r\n')
        sleep(1)

    # 获取上传信息
    def page_get_publish_title(self):
        return self.base_get_text(page.mp_publish_begin_title)

    # 上传开题报告组合业务
    def page_upload_proposal(self, url):
        self.page_click_publish_begin()
        self.page_click_publish_button(url)

