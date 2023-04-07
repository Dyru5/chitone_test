import os,sys

# from Public.Module.log import Log
from selenium import webdriver
from Config.file_dir import CONFIG_DIR
from Public.Module.getyaml import Getyaml
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 读取config.yaml信息
config_path=CONFIG_DIR
Getconfig= Getyaml(config_path)
config=Getconfig.get_yaml()
login_url=config['weburl']['b_url_test']
Br_type=config['browser']['br_default']
# log=Log()

class Page:
    def __init__(self,webdriver,url=login_url,br_type=Br_type):
        '''
        页面基础类，用于其他页面对象的继承
        :param webdriver: webdriver类的实例
        :param url: 网址url
        :param br_type: 浏览器类型
        '''
        self.driver=webdriver
        self.url=url
        self.br_type=br_type

    def openbr(self):
        '''
        打开浏览器
        :param
        :return
        '''
        try:
            self.driver= getattr(webdriver,self.br_type)()
        except Exception as e:
            print(e,"无法识别的浏览器类型{0}，默认选择Chrome浏览器".format(self.br_type))
            self.driver=webdriver.Chrome()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        assert self.driver.current_url == self.url, log.error('Did not land on %s' % self.url)

    def closebr(self):
        '''
        关闭浏览器
        :param
        :return
        '''
        self.driver.quit()

    def find_element(self,loc):
        '''
        定位页面元素
        :param loc: 元素定位方式和位置
        :return: 定位到的元素
        '''
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print("{0}页面中未能找到{1}元素".format(self,loc[1]))
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
        # return self.driver.find_element(*loc)

    def op_element(self,loc,isClick=True,value=None):
        '''
        页面控件操作
        :param loc: 元素定位方式和位置
        :param isClick: 控件类型，True为可点击，False为文本输入框
        :param value: 输入框待输入文本
        :return:
        '''
        try:
            if isClick:
                # 按钮、勾选框操作
                self.find_element(loc).click()
            else:
                # 输入框操作
                self.find_element(loc).clear()
                self.find_element(loc).send_keys(value)
        except AttributeError as ae:
            print(ae,"%s 页面中未能找到 %s 元素" % (self, loc[1]))

    def switch_windows(self,loc):
        '''
        多窗口切换
        :param loc: 元素定位方式和位置
        '''
        try:
            return self.driver.switch_to_window(loc)
        except NoSuchWindowException as msg:
            print("查找窗口句柄handle异常->{0}".format(msg))

    def swicth_alert(self):
        '''
        聚焦到弹出框
        :param
        :return
        '''
        try:
            return self.driver.switch_to_alert()
        except NoAlertPresentException as msg:
            print("查找弹出框异常->{0}".format(msg))

    def switch_frame(self,loc):
        '''
        多层网页iframe切换
        :param loc: 元素定位方式和位置
        :return
        '''
        try:
            return self.driver.switch_to_frame(loc)
        except NoSuchFrameException as msg:
            print("查找iframe异常->{0}".format(msg))

    def script(self,src):
        '''
        提供调用JavaScript方法
        :param src: 脚本文件
        :return: JavaScript脚本
        '''
        return self.driver.execute_script(src)

# driver=webdriver
# pg=Page(driver,br_type='Ie')
# pg.openbr()
# # pg.closebr()
