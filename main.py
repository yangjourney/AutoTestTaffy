# -*- coding: utf-8 -*-
'''
Created on 2016-7-26
@author:
Project:整合自动发邮件功能，执行测试用例生成最新测试报告，取最新的测试报告，发送最新测试报告
问题，邮件始终不能显示html：将电脑时间改为北京时间即可
'''
from HTMLTestRunner import HTMLTestRunner
import time,os,unittest,smtplib,datetime,sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

#1.产生测试套件
def createSuite():
    testunit=unittest.TestSuite()
    #使用discover找出用例文件夹下test_case的所有用例
    #测试模块的顶层目录，即测试用例不是放在多级目录下，设置为none
    if sys.argv[1] == '1':
        discover=unittest.defaultTestLoader.discover('./Tests/AutoAPITests/',pattern='test_*.py', top_level_dir=None)
    elif sys.argv[1] == '2':
        discover=unittest.defaultTestLoader.discover('./Tests/AutoUITests/',pattern='test_*.py', top_level_dir=None)

    #使用for循环出suite,再循环出case
    for suite in discover:
        for case in suite:
            testunit.addTests(case)
    return testunit
discover=createSuite()

#2.定义：取最新测试报告
def new_file(test_dir):
    #列举test_dir目录下的所有文件，结果以列表形式返回。
    lists=os.listdir(test_dir)
    #sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    #最后对lists元素，按文件修改时间大小从小到大排序。
    lists.sort(key=lambda fn:os.path.getmtime(test_dir+'\\'+fn))
    #获取最新文件的绝对路径
    file_path=os.path.join(test_dir,lists[-1])
    return file_path

#3.定义：发送邮件，发送最新测试报告html
def send_email(newfile):
    #打开文件
    f=open(newfile,'rb')
    #读取文件内容
    mail_body=f.read()
    #关闭方法
    f.close()
    #发送邮箱用户名/授权码
    #QQ邮箱的授权码需要登录QQ邮箱，开启POP/SMTP服务，然后获取授权码即可使用，否则无法发送邮件
    user = '303209871@qq.com'
    password='qjsmkirroceybjfd'
    #发送邮箱
    #多个接收邮箱使用逗号分割（,），单个收件人的话，直接是receiver='XXX@xxx.com'
    #Example：receiver=['yangbo145@qq.com','henrysxyh@qq.com']
    receiver=['yangbo145@qq.com']
    #发送邮件主题
    Strtime = datetime.datetime.now().strftime('%Y-%m-%d')
    subject = '自动定时发送测试报告'+ Strtime
    #编写 HTML类型的邮件正文
    #注意：由于msg_html在msg_plain后面，所以msg_html以附件的形式出现
    msg=MIMEMultipart('mixed')
    msg['From'] = u'Jenkins定时执行反馈'
    msg_html1 = MIMEText(mail_body,'html','utf-8')
    msg.attach(msg_html1)
    msg_html = MIMEText(mail_body,'html','utf-8')
    msg_html["Content-Disposition"] = 'attachment; filename='+filename
    msg.attach(msg_html)
    msg['Subject']=Header(subject,'utf-8')
    #连接发送邮件
    try:
        smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)
        smtp.login(user, password)
        smtp.sendmail(user, receiver, msg.as_string())
        smtp.quit()
    except smtplib.SMTPException as e:
        print ("Falied,%s"%e)

#4. 执行用例
if __name__=='__main__':
    print ('=====AutoTest Start======')
    now=time.strftime('%Y-%m-%d_%H_%M_%S_')
    if sys.argv[1] == '1':
        filename = './Report/'+'\\'+ now + 'API_Result.html'
    elif sys.argv[1] == '2':
        filename = './Report/'+'\\'+ now + 'UI_Result.html'
    fp=open(filename ,'wb')
    runner = HTMLTestRunner(stream=fp,title=u'Test Report',description=u'Case Execution Details:')
    runner.run(discover)
    fp.close()
    new_report=new_file('./Report/')
    send_email(new_report)
    print ('=====AutoTest Over======')
