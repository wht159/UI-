from selenium.webdriver.common.by import By

url = 'http://localhost:8080/login'
# 用户名
mp_username = (By.CSS_SELECTOR, "[placeholder='请输入用户名']")
# 验证码
mp_password = (By.CSS_SELECTOR, " [placeholder='请输入密码']")
# 登录按钮
mp_login_btn = (By.CSS_SELECTOR, "#login")
# 角色
mp_role = (By.CSS_SELECTOR, '#role')

# 登录弹出栏
mp_alert = (By.CSS_SELECTOR, '[role="alert"] > p')
# 登录输入框警告
mp_form_item_error = (By.CSS_SELECTOR, '.el-form-item__error')

"""以下为上传课题的定位元素"""

# 上传课题
mp_publish_title = (By.XPATH, "//span[text()= '上传课题']/..")
# 课题名称
mp_title_name = (By.CSS_SELECTOR, "#title_name")
# 课题难度
mp_title_degree = (By.CSS_SELECTOR, "[placeholder='请选择课题难度']")
# 课题类型
mp_title_type = (By.CSS_SELECTOR, "[placeholder='请选择课题类型']")
# 课题来源
mp_title_type = (By.CSS_SELECTOR, "[placeholder='请选择课题来源']")
# 课题摘要
mp_title_abstract = (By.CSS_SELECTOR, "#title_abstract")
# 发布课题
mp_submit_title = (By.XPATH, "//*[text()= '发布课题']/..")
# 结果
mp_result = (By.XPATH, "//p[contains(text(), '发布课题')]")

"""以下为添加成绩的定位元素"""
# 上传课题
mp_add_score = (By.XPATH, "//span[text()= '添加成绩']/..")
# 选择学生
mp_select_student = (By.CSS_SELECTOR, "[placeholder='请选择']")
# 添加成绩
mp_score = (By.CSS_SELECTOR, "#score")
# 发布课题
mp_submit_score = (By.XPATH, "//*[text()= '确认添加']/..")
