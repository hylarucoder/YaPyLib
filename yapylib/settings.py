"""
设置
1. 日志配置
2. 测试
"""
import os
import yaml
import jinja2
from jinja2 import Environment
from dotenv import load_dotenv

load_dotenv()

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
CURRENT_DIR = os.path.curdir
LOGS_FILE = os.path.expanduser("~/.yapylib.log")
TEMPLATE_DIR = os.path.join(ROOT_DIR, 'yapylib/templates')
# config_file = os.path.expanduser("~/.yapylib.yml")
# if not os.path.expanduser(config_file):
#     raise Exception("请设置配置文件")
# else:
#     pass
# with open(config_file, 'r') as f:
#     g_config = yaml.load(f.read())
#
DEBUG = True
USE_COLORS = True

BAIDU_MAP_AK = "---"
TENCENT_MAP_AK = "---"
AMAP_AK = "---"

MAIL_SERVER = "---"
MAIL_USE_SSL = "---"
MAIL_USERNAME = "---"
MAIL_PASSWORD = "---"
MAIL_DEFAULT_SENDER = "---"

SENDER = "123"
#
RECEIVERS = "--"
#
DB_CONNECT_STRING = "--"

loader = jinja2.FileSystemLoader(searchpath=TEMPLATE_DIR)
JINJA2_ENV = Environment(loader=loader)

__all__ = ["g_config"]
