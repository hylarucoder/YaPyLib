def notify(title, subtitle, info_text, delay=0, sound=False, userInfo={}):
    import Foundation, objc

    NSUserNotification = objc.lookUpClass('NSUserNotification')
    NSUserNotificationCenter = objc.lookUpClass('NSUserNotificationCenter')
    """
    Python method to show a desktop notification on Mountain Lion. Where:
    title: Title of notification
    subtitle: Subtitle of notification
    info_text: Informative text of notification
    delay: Delay (in seconds) before showing the notification
    sound: Play the default notification sound
    userInfo: a dictionary that can be used to handle clicks in your
    app's applicationDidFinishLaunching:aNotification method
    """
    notification = NSUserNotification.alloc().init()
    notification.setTitle_(title)
    notification.setSubtitle_(subtitle)
    notification.setInformativeText_(info_text)
    notification.setUserInfo_(userInfo)
    if sound:
        notification.setSoundName_("NSUserNotificationDefaultSoundName")
    notification.setDeliveryDate_(Foundation.NSDate.dateWithTimeInterval_sinceDate_(delay, Foundation.NSDate.date()))
    NSUserNotificationCenter.defaultUserNotificationCenter().scheduleNotification_(notification)


"""
下面的程序主要用于MacOS上一些程序的调用
"""


def open_image():
    pass


def open_url():
    pass


def open_video():
    pass


import sys
import uuid
import socket
from collections import OrderedDict
from urllib.request import urlopen

import re

import time

from yapylib.logging import get_logger
import getpass

from yapylib.helpers.datetime import cur_time


def check_setting_and_env():
    """
    当前运行环境:
    1. 操作系统版本
    2. 数据库(PostgreSQL)以及数据库版本
    3. Python
    4. 当前路径
    5. 当前用户
    :return:
    """
    try:
        url = "http://ip.chinaz.com/getip.aspx"
        like_json_html = urlopen(url).read().decode("utf-8")
        groups = re.match("\{ip:'(.+)',address:'(.+)'\}", like_json_html).groups()
        # print(groups)
        external_ip_info = groups
        external_ip = groups[0]
        if external_ip is None:
            external_ip_info = "offline"
    except Exception:
        external_ip_info = "offline"
        pass

    infos = OrderedDict()
    infos["Python版本"] = sys.version.split()[0]
    infos["操作系统"] = get_current_os()
    infos["内网IP为"] = get_internal_ip()
    infos["外网IP为"] = " - ".join(external_ip_info)
    infos["当前工作路径"] = os.getcwd()
    infos["当前用户"] = getpass.getuser()
    for k, v in infos.items():
        get_logger("project").info("{} : {}".format(k, v))

    if sys.version_info < (3, 4):
        raise RuntimeError("at least Python 3.5 is required!!")


def get_current_os():
    name = os.name
    if 'posix' in name:
        return "Mac OS"
    elif 'linux' in name:
        return "Linux"
    else:
        return "Windows"


def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])


def get_internal_ip():
    try:
        return socket.gethostbyname(socket.getfqdn(socket.gethostname()))
    except Exception:
        return "0.0.0.0"


def clear_terminal():
    print(chr(27) + "[2J")


import os, psutil


def memory_usage():
    process = psutil.Process(os.getpid())
    return process.get_memory_info()[0] / float(2 ** 20)


def restart_if_failed(func, max_tries, args=(), kwargs={}, secs=60, sleep=None):
    """
    https://github.com/lilydjwg/winterpy/blob/master/pylib/myutils.py
    :param func:
    :param max_tries:
    :param args:
    :param kwargs:
    :param secs:
    :param sleep:
    :return:
    re-run when some exception happens, until `max_tries` in `secs`
    """
    import traceback
    from collections import deque

    dq = deque(maxlen=max_tries)
    while True:
        dq.append(cur_time())
        try:
            func(*args, **kwargs)
        except:
            traceback.print_exc()
            if len(dq) == max_tries and cur_time() - dq[0] < secs:
                break
            if sleep is not None:
                time.sleep(sleep)
        else:
            break
