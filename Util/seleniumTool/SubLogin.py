# coding=utf-8
from Util.seleniumTool import BasePage

class SubLogin(BasePage.BasePage):
    def __init__(self, driver, baseUrl):
        """
        :param driver:
        :param baseUrl:
        """
        # 调用其 基类 BasePage的 构造函数
        # 实现 基类 的构造函数的功能
        BasePage.BasePage.__init__(self,driver, baseUrl)
        self.loginPageUrl = "login"
        self.driver.clearCookies()

    def login(self,userName,password):
        self.openPage(self.loginPageUrl)
        # self.driver.clearCookies()
        self.driver.wait(5)
        self.driver.send_keys("xpath|.//*[@placeholder='登录名']", userName)
        self.driver.send_keys("xpath|.//*[@placeholder='密码']", password)
        self.driver.click("xpath|.//parent::button")

    def getMainPage(self):
        return self.baseUrl
