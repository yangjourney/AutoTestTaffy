# coding=utf-8
import unittest,os,time
from Common.Selenium_Webdriver import webutils
from Util.seleniumTool.SubLogin import SubLogin

"""
1. 导入 unittest
2. 继承 unittest.TestCase
3. 写用例 方法以  开头
4. 考虑使用 setUp() 和 tearDown()
"""
class Tests(unittest.TestCase):
    def setUp(self):
        """
        开始每个测试前的准备事项
        :return:
        """
        self.autoDriver = webutils("firefox")
        self.autoDriver.max_window()
        self.baseUrl = "http://10.2.5.139:5000/#/"

    def tearDown(self):
        """
        结束每个测试后的清理工作
        :return:
        """
        self.autoDriver.quit()

    def test_login(self):
        """
        测试用例：测试登录
        :return:
        """
        loginPage = SubLogin(self.autoDriver, self.baseUrl)
        time.sleep(4)
        # 利用页面对象进行登录
        loginPage.login("user01", "123456")
        #self.autoDriver.wait(5)
        time.sleep(4)
        # 断言 是否登录成功
        #def login_error(self):
        #print(self.autoDriver.find_element("class,user-name flex-y-center").text)
        #self.assertEqual(self.autoDriver.get_text("class,user-name flex-y-center"), "test01", "测试通过！")
        #try:
        #   errors=self.autoDriver.get_text("class,el-message__group")
        #    if errors=="用户名密码错误2":
        #       return "登录失败!"
        #    else:
        #        return "登录成功！"
        #except:
        #    return "未知错误！"
