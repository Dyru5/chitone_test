import logging,time
import os,sys
from Config.file_dir import LOG_DIR
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
# 如果日志文件不存在，自动创建
if not os.path.exists(LOG_DIR):os.makedirs(LOG_DIR)

class Log():
    def __init__(self):
        '''
        日志记录
        '''
        #日志文件命名
        self.logname=os.path.join(LOG_DIR,'%s.log'%time.strftime('%Y%m%d_%H%M%S'))
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        #日志输出格式
        self.formatter=logging.Formatter('[%(asctime)s] [%(filename)s|%(funcName)s] [line:%(lineno)d] %(levelname)-8s: %(message)s')

    def __console(self,level,msg):
        # 创建一个FileHandler，用于写到本地日志文件
        fh = logging.FileHandler(self.logname,encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 移除日志重复信息
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)