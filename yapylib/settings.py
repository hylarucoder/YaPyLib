"""
设置
1. 日志配置
2. 测试
"""
import os
import yaml
import jinja2
from jinja2 import Environment

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
CURRENT_DIR = os.path.curdir
LOGS_DIR = os.path.join(CURRENT_DIR)
TEMPLATE_DIR = os.path.join(ROOT_DIR, 'yapylib/templates')
config_file = os.path.expanduser("~/.yapylib.yaml")
if not os.path.expanduser(config_file):
    raise Exception("请设置配置文件")
else:
    pass
with open(config_file, 'r') as f:
    g_config = yaml.load(f.read())
    print(g_config)

DEBUG = g_config["DEBUG"]
USE_COLORS = g_config["USE_COLORS"]

BAIDU_MAP_AK = g_config["BAIDU_MAP_AK"]
TENCENT_MAP_AK = g_config["TENCENT_MAP_AK"]
AMAP_AK = g_config["AMAP_AK"]

MAIL_SERVER = g_config["MAIL_SERVER"]
MAIL_USE_SSL = g_config["MAIL_USE_SSL"]
MAIL_USERNAME = g_config["MAIL_USERNAME"]
MAIL_PASSWORD = g_config["MAIL_PASSWORD"]
MAIL_DEFAULT_SENDER = g_config["MAIL_DEFAULT_SENDER"]

SENDER = g_config["SENDER"]

RECEIVERS = g_config["RECEIVERS"]

DB_CONNECT_STRING = g_config["DB_CONNECT_STRING"]

loader = jinja2.FileSystemLoader(searchpath=TEMPLATE_DIR)
JINJA2_ENV = Environment(loader=loader)

__all__ = ["g_config"]
