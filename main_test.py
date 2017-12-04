# -*- coding: utf-8 -*-
'''
Created on 2016-7-26
@author:
Project:整合自动发邮件功能，执行测试用例生成最新测试报告，取最新的测试报告，发送最新测试报告
问题，邮件始终不能显示html：将电脑时间改为北京时间即可
'''
import os
import sys
import time
import unittest
import configparser
from HTMLTestRunner import HTMLTestRunner
from Common.log import logger
from Common.sendmail import MyMail
#rest

#1.产生测试套件
def createSuite():
    testunit=unittest.TestSuite()
    #使用discover找出用例文件夹下test_case的所有用例
    #测试模块的顶层目录，即测试用例不是放在多级目录下，设置为none
    if sys.argv[1] == '1':
        discover=unittest.defaultTestLoader.discover('./Tests/AutoAPITests/',pattern='test_*.py', top_level_dir=None)
        print discover
    elif sys.argv[1] == '2':
        discover=unittest.defaultTestLoader.discover('./Tests/AutoUITests/',pattern='test_*.py', top_level_dir=None)
        print discover

    #使用for循环出suite,再循环出case
    for suite in discover:
        for case in suite:
            testunit.addTests(case)
    return testunit
discover=createSuite()

#2.定义：取最新测试报告
def new_file():
    config = configparser.ConfigParser()
    config.read('./config/report.conf', encoding='utf-8')
    dir_of_report = config['REPORT']['dir_of_report']
    #列举test_dir目录下的所有文件，结果以列表形式返回。

    lists=os.listdir(dir_of_report)
    #sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    #最后对lists元素，按文件修改时间大小从小到大排序。
    lists.sort(key=lambda fn:os.path.getmtime(dir_of_report))
    #获取最新文件的绝对路径
    file_path=os.path.join(dir_of_report,lists[-1])
    return file_path

if __name__=='__main__':

    print new_file()
    mymail = MyMail('./config/mail.conf')
    mymail.connect()
    mymail.login()
    mail_content = 'Hi,Attachments Is Test Report,Please Refer .'
    mail_tiltle = '[Test Report]Test Report'
    #根据配置文件读取测试报告路径，并通过newfile获取最新的测试报告作为附件发送，代码下周更新
    #attachments = set('./Report/')
    logger.info('Building Test Report Success!')
    #attachments = new_file()
    attachments = set([new_file()])
    logger.info('Test Report Sending...')
    mymail.send_mail(mail_tiltle, mail_content, attachments)
    mymail.quit()
    logger.info('Sending Success!')