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
    # 2. 通过统一入口类获取PageMpLogin对象
    mp = PageIn(driver).page_get_pageMpLogin()
    driver.implicitly_wait(2)
    yield mp

    # 调用关闭driver
    GetDriver.quit_web_driver()


@pytest.fixture(scope="function")
def exe_driver_title():
    # 1. 获取driver
    driver = GetDriver.get_web_driver(page.url)
    # 2. 获取统一入口类获取对象
    page_in = PageIn(driver)
    # 3. 获取PageMpLogin对象并调用成功登录依赖的方法
    page_in.page_get_pageMpLogin().page_mp_title_login_success()
    # 4. 获取PageMpTitle页面对象
    title = page_in.page_get_pageMpTitle()
    # 5. 插入前删除语句
    db.execute_db(sql["test_title_sql"])
    log.info("执行前置SQL：{}".format(sql["test_title_sql"]))
    yield title
    # 调用关闭driver

    GetDriver.quit_web_driver()
    # 插入后删除语句
    db.execute_db(sql["test_title_sql"])
    log.info("执行后置SQL：{}".format(sql["test_title_sql"]))


@pytest.fixture(scope="function")
def exe_driver_score():
    # 1. 获取driver
    driver = GetDriver.get_web_driver(page.url)
    # 2. 获取统一入口类获取对象
    page_in = PageIn(driver)
    # 3. 获取PageMpLogin对象并调用成功登录依赖的方法
    page_in.page_get_pageMpLogin().page_mp_title_login_success()
    # 4. 获取page_get_pageMpScore页面对象
    score = page_in.page_get_pageMpScore()
    # driver.implicitly_wait(10)
    # 5. 更改前令成绩为空
    db.execute_db(sql["test_score_sql"])
    log.info("执行前置SQL：{}".format(sql["test_score_sql"]))
    yield score
    # 调用关闭driver
    GetDriver.quit_web_driver()
    db.execute_db(sql["test_score_sql"])
    log.info("执行后置SQL：{}".format(sql["test_score_sql"]))




