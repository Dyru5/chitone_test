import os,sys
import time
import warnings
from random import randint

from Config.file_dir import TESTDATA_DIR
from Public.Module.getyaml import Getyaml, split
from Public.Module.log import Log
from Public.Page.loginpage import LoginPage
from ddt import ddt, data
from selenium import webdriver

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest,yaml
log=Log()
# 获取loginData文件数据
try:
    LoginYaml=Getyaml(TESTDATA_DIR+'\\'+'loginData.yaml')
    loginyaml=LoginYaml.get_yaml()
    logindata=loginyaml['data_test']
except FileNotFoundError as msg:
    print('文件不存在：{0}'.format(msg))

@ddt
class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver
        self.page=LoginPage(self.driver)
        warnings.simplefilter('ignore',ResourceWarning)
        print('\n用例信息：测试用例ID->{0},测试点->{1}'.format(loginyaml['id'],loginyaml['desc']))

    @data(*logindata)
    def test_login(self,data):
        '''
        登录测试
        :param:
        :return:
        '''
        print('用例描述：'+data['desc'])

        if data['type']==1:  #正常登录流程
            self.page.user_login(data['user'],data['pwd'])
            self.page.op_element(self.page.key_Esc) #退出使用教程
            try:
                rr = self.page.login_username_hint() #判断是否成功登录
            except AttributeError:
                print('用例结果：Failed.未成功登录')
                raise
            else:
                er = data['check']
                self.assertEqual(rr, er, '用例结果：Failed.登录账号不匹配，预期登录账号为{0}，实际为{1}'.format(er, rr))
                print('用例结果：Pass!')   #判断登录账号是否一致
        else:   #异常登录流程
            wrandom=str(randint(0,99))
            self.page.user_login(data['user']+wrandom, data['pwd'])
            rr=self.page.login_error_hint()
            er=data['check']
            self.assertEqual(rr,er,'用例结果：Failed.提示信息错误')
            print('用例结果：Pass!')
    def tearDown(self) -> None:
        time.sleep(3)
        self.page.closebr()
        print('----用例测试完成----')

if __name__=='__main__':
    unittest.main()
