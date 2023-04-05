# UI自动化框架

#### 简介

基于selenium,pytest,python的Web自动化测试框架，使用PO设计模式，yaml实现数据驱动

#### 使用

1. 使用python3.10.4版本
2. 拉取源码到本地
3. pip install -r requirements.txt 安装依赖库
4. 修改data文件中driver.yaml的url和浏览器
5. 下载并配置响应浏览器的驱动
6. 修改pytest.ini配置
7. 控制台输入pytest

#### 实现功能

- 底层全部采用显示等待，提高框架执行效率
- 使用单例模式获取driver
- 测试失败截图，并加入allure报告
- 用例失败重跑
- 采用通用配置文件，增强框架可维护性
- 采用yaml文件管理测试数据
- 采用类管理元素定位，方便后期维护

 

