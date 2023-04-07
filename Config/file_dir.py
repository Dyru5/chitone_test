# 文件路径设置
import os,sys

# 获取项目根目录作为基础路径
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
# 将BASE_DIR加入可引用模块
sys.path.append(BASE_DIR)

# 配置文件
CONFIG_DIR=os.path.join(BASE_DIR,"Config","config.yaml")
# 页面元素控件
PAGEELE_DIR=os.path.join(BASE_DIR,"PageEle")
# 测试数据
TESTDATA_DIR=os.path.join(BASE_DIR,"TestData")
# 测试用例
TESTCASE_DIR=os.path.join(BASE_DIR,"TestCase")
# 测试报告
REPORT_DIR=os.path.join(BASE_DIR,"Report")
# 日志
LOG_DIR=os.path.join(BASE_DIR,"Log")
