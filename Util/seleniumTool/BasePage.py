# coding=utf-8
class BasePage():
    def __init__(self, webutils, baseUrl):
        """
        构造方法
        :param driver: 封装好的webdriver
        :param baseUrl:
        """
        self.baseUrl = baseUrl
        self.driver = webutils

    def openPage(self, url):
        """
        打开系统的页面，通过拼接URL的方式
        :param url:
        :return:
        """
        self.driver.get(self.baseUrl + url)