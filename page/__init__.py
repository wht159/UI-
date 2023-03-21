from selenium.webdriver.common.by import By

url = 'http://localhost:8080/login'
# 用户名
mp_username = (By.CSS_SELECTOR, "[placeholder='请输入用户名']")
# 密码
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

"""以下为上次开题报告的定位元素"""
# 上传开题报告
mp_publish_begin = (By.XPATH, "//span[text()= '提交开题报告']/..")
# 上传开题报告
mp_publish_button = (By.XPATH, "//button[@class='el-button ml-5 el-button--primary el-button--mini']")
# 上传开题报告名称获取
mp_publish_begin_title = (By.XPATH, "//*[@id='appendix']")

"""以下为注册的定位元素"""
# 进入学生注册按钮
mp_student_register_button = (By.XPATH, "//*[text()= '学生注册']/..")
# 进入导师注册按钮
mp_teacher_register_button = (By.XPATH, "//*[text()= '导师注册']/..")
# 用户名
mp_register_username = (By.XPATH, "//input[@placeholder='请输入账号']")
# 密码
mp_register_password = (By.XPATH, "//input[@placeholder='请输入密码']")
# 确认密码
mp_confirm_password = (By.XPATH, "//input[@placeholder='请确认密码']")
# 姓名
mp_register_name = (By.XPATH, "//input[@placeholder='请输入姓名']")
# 学号
mp_register_sno = (By.XPATH, "//input[@placeholder='请输入学号']")
# 工号
mp_register_tno = (By.XPATH, "//input[@placeholder='请输入工号']")
# 院系
mp_register_department = (By.XPATH, "//input[@placeholder='请输入所在院系']")
# 注册按钮
mp_confirm_register_button = (By.XPATH, "//span[text()= '注册']/..")
# 学号提醒信息
mp_sno_alter = (By.XPATH, "//*[@id='app']/div/div/form/div[6]/div/div[2]")

"""管理员选择学生的导师定位元素"""

# 点击学生管理
mp_student_manager = (By.XPATH, "//span[text()= '学生管理']/..")
# 获取输入学号输入框
mp_input_sno = (By.XPATH, "//input[@placeholder='请输入学号']")
# 点击搜索学号
mp_select_sno_button = (By.XPATH, "//span[text()= '搜索']/..")
# 点击选择指导老师
mp_select_Teacher_button = (By.XPATH, "//span[text()= ' 选择指导老师 ']/..")
# 点击确定
mp_confirm_select_Teacher_button = (By.XPATH, "//*[@id='app']/section/section/main/div/div[5]/div/div[3]/div/button[2]")
# 获取选择结果
mp_select_teacher_result = (By.XPATH, "//*[@id='app']/section/section/main/div/div[2]/div[3]/table/tbody/tr/td[9]/div")

"""导师审核论文元素定位"""

# 点击审核毕业论文
mp_click_verify_manager = (By.XPATH, "//span[text()= '审核毕业论文']/..")
# 点击查重按钮
mp_click_check_paper = (By.XPATH, "//div[text()='student3']/../../td[6]/div/button[2]")
# 获取查重信息
mp_check_info = (By.XPATH, "//div[text()= '本科毕业单击选择名称.docx']/../../td[3]/div")
# 点击审核按钮
mp_click_verify_paper = (By.XPATH, "//div[text()='student3']/../../td[6]/div/button")
# 点击审核通过
mp_verify_success = (By.XPATH, "//*[text()='通过']/../span/input")
# 点击审核不通过
mp_verify_fail = (By.XPATH, "//*[text()='不通过']/../span/input")
# 输入审核意见
mp_input_comment = (By.XPATH, "//textarea")
# 审核提交按钮
mp_verify_submit = (By.XPATH, "//span[text()='提交']/..")
