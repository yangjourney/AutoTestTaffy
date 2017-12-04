# -*- coding: utf-8 -*-
"""
FuncName: webutils.py
Desc: committed to a simpler automated testing,based on the original selenium.
Date:
Home:
Author:
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

class webutils(object):
    """
        webutils framework are committed to a simpler automated testing,
    based on the original selenium.
    """

    def __init__(self, browser):
        """
        说明：

        初始化方法，默认使用firefox，当然，在使用过程中也可以使用chrome、ie

        用法：
        webutils("chrome")
        注意事项：
        chrome浏览器需要对应的驱动程序，各个驱动程序对应的chrome版本不同，其对应版本如下：
        chromedriver版本     支持的Chrome版本
            v2.33         v60-62
            v2.32         v59-61
            v2.30~31         v58-60
            v2.29         v56-58
            v2.28         v55-57
            v2.27         v54-56
            v2.26         v53-55
            v2.25         v53-54
            v2.24         v52-54
            v2.23         v51-53
            v2.22         v49-52
            v2.21         v46-50
            v2.20         v43-48
            v2.19         v43-47
            v2.18         v43-46
            v2.17         v42-43
            v2.13         v42-45
            v2.15         v40-43
            v2.14         v39-42
            v2.13         v38-41
            v2.12         v36-40
            v2.11         v36-40
            v2.10         v33-36
            v2.9          v31-34
            v2.8          v30-33
            v2.7          v30-33
            v2.6          v29-32
            v2.5          v29-32
            v2.4          v29-32
        """
        if browser == "firefox" :
            driver = webdriver.Firefox()
        elif browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "ie" :
            driver = webdriver.Ie()
        try:
            self.driver = driver
        #    self.driver=getattr(webdriver,browser.capitalize())()
        except Exception:
            raise NameError("Not found this browser,You can enter 'firefox', 'chrome', 'ie' .")

    def get(self, url):
        """
        说明：

                打开 url

        用法:
        driver.get("http://www.baidu.com")
        """
        self.driver.get(url)

    def max_window(self):
        """
        说明：

                设置浏览器最大化

        用法:
        driver.max_window()
        """
        self.driver.maximize_window()

    def set_window_size(self, wide, high):
        """
        说明：

                设置浏览器宽度和高度

        用法:
        driver.set_window_size(wide,high)
        """
        self.driver.set_window_size(wide, high)

    def wait(self, secsonds):
        """
         说明：

               智能等待（隐式等待），全局

        用法:
        driver.wait(10)
        """
        self.driver.implicitly_wait(secsonds)

    def find_element(self,element):
        """
        说明：

                设置元素定位方式，如：id、css、xpath、class

        用法:
        driver.find_element("id|kw")
        """
        if "|" not in element:
            raise NameError("SyntaxError: invalid syntax, lack of '|'.")

        by = element.split("|")[0]
        value = element.split("|")[1]

        if by == "id":
            return self.driver.find_element_by_id(value)
        elif by == "name":
            return self.driver.find_element_by_name(value)
        elif by == "class":
            return self.driver.find_element_by_class_name(value)
        elif by == "text":
            return self.driver.find_element_by_link_text(value)
        elif by == "text_part":
            return self.driver.find_element_by_partial_link_text(value)
        elif by == "xpath":
            return self.driver.find_element_by_xpath(value)
        elif by == "css":
            return self.driver.find_element_by_css_selector(value)
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','text','xpath','css'.")

    def wait_element(self, element, seconds=5):
        """
        说明：

                等待元素加载

        使用场景在编码过程中根据实际情况选择使用：一般运用于页面加载较慢，网络不畅等一些特殊场景，

        用法:
        driver.wait_element("id|kw",10)
        """
        if "|" not in element:
            raise NameError("SyntaxError: invalid syntax, lack of '|'.")

        by = element.split("|")[0]
        value = element.split("|")[1]

        if by == "id":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.ID, value)))
        elif by == "name":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.NAME, value)))
        elif by == "class":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
        elif by == "text":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
        elif by == "xpath":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.XPATH, value)))
        elif by == "css":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','text','xpaht','css'.")

    def send_keys(self, element, text):
        """
        说明：

        清除元素内容后执行输入操作

        用法:
        driver.send_keys("id|kw","selenium")
        """
        self.wait_element(element)
        self.find_element(element).clear()
        self.find_element(element).send_keys(text)

    def click(self, element):
        """
        说明：

        点击任何文字/图片可以点击，连接，复选框，单选按钮，甚至下拉框等。

        用法:
        driver.click("id|kw")
        """
        self.wait_element(element)
        self.find_element(element).click()

    def right_click(self, element):
        """
        说明：

        右键点击页面元素

        用法:
        driver.right_click("class|right")
        """
        self.wait_element(element)
        ActionChains(self.driver).context_click(self.find_element(element)).perform()

    def move_to_element(self, element):
        '''
        说明：

        将鼠标移动到元素上方

        用法:
        driver.move_to_element("css|choose")
        '''
        self.wait_element(element)
        ActionChains(self.driver).move_to_element(self.find_element(element)).perform()

    def double_click(self, element):
        """
        说明：

        双击选定的页面元素

        用法:
        driver.double_click("name|baidu")
        """
        self.wait_element(element)
        ActionChains(self.driver).double_click(self.find_element(element)).perform()

    def drag_and_drop(self, source_element, target_element):
        """
        说明：

        拖动一个元素一定的位置后放开。

        用法:
        driver.drag_and_drop("id|s","id|t")
        """
        self.wait_element(source_element)
        self.wait_element(target_element)
        ActionChains(self.driver).drag_and_drop(self.find_element(source_element), self.find_element(target_element)).perform()

    def back(self):
        """
        说明：

        返回上一层窗口

        用法:
        driver.back()
        """
        self.driver.back()

    def forward(self):
        """
        说明：

        跳转到上一层窗口

        用法:
        driver.forward()
        """
        self.driver.forward()

    def get_attribute(self, element, attribute):
        """
        说明：

        获取页面元素的属性值。

        用法:
        driver.get_attribute("id|kw","attribute")
        """
        self.wait_element(element)
        return self.find_element(element).get_attribute(attribute)

    def get_text(self, element):
        """
        说明：

        获取页面元素的文本信息。

        用法:
        driver.get_text("name|johnny")
        """
        self.wait_element(element)
        return self.find_element(element).text

    def get_display(self, element):
        """
        说明：

        获取要显示的元素，返回结果为true或false。

        用法:
        driver.get_display("id|ppp")
        """
        self.wait_element(element)
        return self.find_element(element).is_displayed()

    def get_title(self):
        """
        说明：

        获取窗口标题。

        用法:
        driver.get_title()
        """
        time.sleep(2)
        return self.driver.title

    def get_url(self):
        """
        说明：

        获取当前页的URL地址。

        用法:
        driver.get_url()
        """
        return self.driver.current_url

    def get_screenshot(self, file_path):
        """
        说明：

        获取当前窗口截图。

        用法:
        driver.get_screenshot("./pic.png")
        """
        self.driver.get_screenshot_as_file(file_path)

    def submit(self, element):
        """
        说明：

        提交指定表格。

        用法:
        driver.submit("id|mainFrame")
        """
        self.wait_element(element)
        self.find_element(element).submit()

    def switch_to_frame(self, element):
        """
        说明：

        切换到特定的frame。

        用法:
        driver.switch_to_frame("id|mainFrame")
        """
        self.wait_element(element)
        self.driver._switch_to_frame(self.find_element(element))

    def clearCookies(self):
        """
        说明：

        在初始化浏览器的时候清除所有的cookies

        用法:
        self.driver.clearCookies()
        """
        self.driver.delete_all_cookies()


    def switch_to_frame_out(self):
        """
        说明：

        切换默认的上下文。

        用法:
        driver.switch_to_frame_out()
        """
        self.driver.switch_to.default_content()

    def open_new_window(self, element):
        """
        说明：

        打开新窗口并将句柄切换到新打开的窗口。

        用法:
        driver.open_new_window(id|johnny)
        """
        current_windows = self.driver.current_window_handle
        self.find_element(element).click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != current_windows:
                self.driver.switch_to.window(handle)
    def F5(self):
        '''
        说明：

        刷新当前页面。

        用法:
        driver.F5()
        '''
        self.driver.refresh()

    def js(self, script):
        """
        说明：

        执行JavaScript脚本。

        用法:
        driver.js("window.scrollTo(200,1000);")
        """
        self.driver.execute_script(script)

    def accept_alert(self):
        """
        说明：

        确认按钮

        用法:
        driver.accept_alert()
        """
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """
        说明：

        取消对话框

        用法:
        driver.dismiss_alert()
        """
        self.driver.switch_to.alert.dismiss()

    def close(self):
        """
        说明：

        关闭当前窗体。

        用法:
        driver.close()
        """
        self.driver.close()

    def quit(self):
        """
        说明：

        退出该驱动程序并关闭所有窗口。

        用法:
        driver.quit()
        """
        self.driver.quit()
