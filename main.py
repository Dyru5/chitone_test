import time
import unittest

from Config.file_dir import TESTCASE_DIR, REPORT_DIR
from Package.HTMLTestRunner import HTMLTestRunner
from Public.Module.sendmail import SendMail
from Public.Page.basepage import Br_type

discover= unittest.defaultTestLoader.discover(TESTCASE_DIR,pattern='*test.py')
now=time.strftime('%Y-%m-%d %H-%M-%S')
filename=REPORT_DIR+'\\'+now+'report.html'
with open(filename,'wb+') as f:
    runner=HTMLTestRunner(stream=f,verbosity=2,title='Job5156自动化测试报告',description='测试环境：Windows10+{0}'.format(Br_type),tester='魏东宇')
    runner.run(discover)

# 发送邮件，需要发送邮件时启用
# Mail=SendMail(file=filename)
# Mail.send_mail()