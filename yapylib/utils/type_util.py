"""
Python类型判断
文本内容判断
图片类型判断
"""

import json


def is_str(value):
    return isinstance(value, str)


def is_float(value):
    return isinstance(value, float)


def is_int(value):
    return isinstance(value, int)


def is_json(_str):
    try:
        json.loads(_str)
    except ValueError as e:
        return False
    return True


def is_html(_str):
    try:
        from bs4 import BeautifulSoup
        BeautifulSoup(_str, 'lxml')
    except ValueError as e:
        return False
    return True
