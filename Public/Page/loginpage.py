import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from selenium import webdriver
from Config.file_dir import PAGEELE_DIR
from Public.Module.getyaml import Getyaml
from Public.Page.basepage import Page
from selenium.webdriver.common.by import By

# 登录页控件
Get_login_Ele=Getyaml(PAGEELE_DIR + '\\' + 'loginEle.yaml')
loginPageEle=Get_login_Ele.get_yaml()

class LoginPage(Page):
    '''
    登录页类
    '''
    # 用户名输入框
    login_user_loc=(By.XPATH,loginPageEle['testele'][0]['element_info'])
    # 密码输入框
    login_pwd_loc=(By.XPATH,loginPageEle['testele'][1]['element_info'])
    # 自动登录单选框
    login_auto_loc=(By.XPATH,loginPageEle['testele'][2]['element_info'])
    # 单击登录
    login_button_loc=(By.XPATH,loginPageEle['testele'][3]['element_info'])
    # ESC退出提示
    key_Esc=(By.CSS_SELECTOR,'.esc')

    # 登录失败错误提示
    login_error_hint_loc=(By.XPATH,loginPageEle['checkele'][0]['element_info'])
    # 登录成功用户名
    login_username_hint_loc=(By.XPATH,loginPageEle['checkele'][1]['element_info'])

    def user_login(self,user,pwd):
        '''
        用户名密码登录
        :param user: 用户名
        :param pwd: 密码
        :return: 操作后当前的网页
        '''
        self.openbr()
        self.driver.implicitly_wait(10)
        self.op_element(self.login_user_loc,False,user)
        self.op_element(self.login_pwd_loc,False,pwd)
        self.op_element(self.login_auto_loc)
        self.op_element(self.login_button_loc)
        self.driver.implicitly_wait(10)
        return self.driver

    def login_error_hint(self):
        '''
        获取登录失败提示信息
        :param
        :return: 登录失败提示文本
        '''
        return self.find_element(self.login_error_hint_loc).text

    def login_username_hint(self):
        '''
        获取登录成功后的账户用户名
        :param
        :return: 登录成功后的账户用户名
        '''
        return self.find_element(self.login_username_hint_loc).text

    def closepage(self):
        '''
        关闭当前网页
        :param
        :return
        '''
        self.driver.close()
# print(loginPageEle)
