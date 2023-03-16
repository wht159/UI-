from page.page_mp_addScore import PageMpAddScore
from page.page_mp_login import PageMpLogin
from page.page_mp_title import PageMpTitle


class PageIn:
    def __init__(self, driver):
        self.driver = driver

    # 获取PageMpLogin对象
    def page_get_pageMpLogin(self):
        return PageMpLogin(self.driver)

    # 获取PageMpTitle对象
    def page_get_pageMpTitle(self):
        return PageMpTitle(self.driver)

    # 获取PageMpTitle对象
    def page_get_pageMpScore(self):
        return PageMpAddScore(self.driver)