import yaml
from Config.file_dir import CONFIG_DIR
from selenium.webdriver.common.by import By


class Getyaml:
    def __init__(self,file):
        self.file=file
    def get_yaml(self):
        # 加载yaml文件数据
        try:
            f=open(self.file,encoding='utf-8')
            data=yaml.load(f,Loader=yaml.FullLoader)
            f.close()
            return data
        except Exception as msg:
            print("异常消息->{0}".format(msg))

def split(list,key):
    '''
    将字典数组中所有相同key的value存储为新的列表
    :param list: 需要操作的字典数组
    :param key:需要另外存储内容的key
    :return：新的数组
    '''
    nlist=[]
    for dict in list:
        nlist.append(dict[key])
    return nlist

def opt_remark_to_loc(options,optremark):
    '''
    根据opt_remark内容返回对应的定位loc
    :param opt: 需要操作的options数组
    :param optremark: options数组中的opt_remark
    :return: 元素定位loc
    '''
    loc=None
    for opt in options:
        if opt['opt_remark']==optremark:
            loc=(By.XPATH,opt['opt_info'])
    return loc

