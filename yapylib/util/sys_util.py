import logging

import sys

logger = logging.getLogger("logger_root")


def check_setting_and_env():
    """
    当前运行环境:
    1. 操作系统版本
    2. 数据库(MySQL,Redis)以及数据库版本
    3. Python
    4. 当前路径
    5. 当前用户
    :return:
    """
    if sys.version_info < (3, 4):
        raise RuntimeError("at least Python 3.5 is required!!")


import uuid
import socket


def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])


def get_internal_ip():
    return socket.gethostbyname(socket.getfqdn(socket.gethostname()))


def clear_terminal():
    print(chr(27) + "[2J")
