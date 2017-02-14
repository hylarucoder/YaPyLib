"""
1. 字符串/数组/balbla安全json化
2. 字符串化
"""

import json


def is_json(_str):
    try:
        json_obj = json.loads(_str)
    except ValueError as e:
        return False
    return True


def safe_jsonfy(_str):
    pass
