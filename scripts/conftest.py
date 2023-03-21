import pytest
import page
from base.base import log
from page.page_in import PageIn
from tools.con_sql import db
from tools.get_driver import GetDriver
from tools.read_yaml import read_yaml

sql = read_yaml("mp_sql.yaml")


@pytest.fixture(scope="function")
def exe_driver():
    # 1. 获取driver
    driver = GetDriver.get_web_driver(page.url)
    driver.implicitly_wait(3)
    yield driver
    # 调用关闭driver
    GetDriver.quit_web_driver()





