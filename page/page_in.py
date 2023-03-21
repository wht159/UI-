from page.page_mp_addScore import PageMpAddScore
from page.page_mp_admin import PageUpAdmin
from page.page_mp_login import PageMpLogin
from page.page_mp_register import PageMpRegister
from page.page_mp_title import PageMpTitle
from page.page_mp_upload import PageUpLoad
from page.page_mp_verify import PageVerify


class PageIn:
    def __init__(self, driver):
        self.driver = driver

    # 获取PageMpLogin对象
    def page_get_pageMpLogin(self):
        return PageMpLogin(self.driver)

    # 获取PageMpTitle对象
    def page_get_pageMpTitle(self):
        return PageMpTitle(self.driver)

    # 获取PageMpScore对象
    def page_get_pageMpScore(self):
        return PageMpAddScore(self.driver)

    # 获取PageMpUpload对象
    def page_get_pageMpUpload(self):
        return PageUpLoad(self.driver)

    # 获取PageMpRegister对象
    def page_get_pageMpRegister(self):
        return PageMpRegister(self.driver)

    # 获取PageMpUpload对象
    def page_get_pageMpAdmin(self):
        return PageUpAdmin(self.driver)

    # 获取PageMpUpload对象
    def page_get_pageMpVerify(self):
        return PageVerify(self.driver)