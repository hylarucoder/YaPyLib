"""
对常见字典数据结构进行封装
1. 翻转可翻转字典
2. 排除字典指定
"""
import operator
from collections import OrderedDict


def extract_dicts_exclude_keys(_dicts, keys):
    for _dict in _dicts:
        for key in keys:
            _dict.pop(key)
    return _dicts


def reverse_dict(_dict):
    if len(_dict.keys()) == len(_dict.values()):
        return {v: k for k, v in _dict.items()}
    else:
        raise ValueError("字典有重复值")


def merge_two_dicts(x, y):
    """
    python 3.5 only
    :param x: 
    :param y: 
    :return: 
    """
    return {**x, **y}


def sort_dict_by_key(_dict, transpose=False):
    if transpose is False:
        sorted_x = sorted(_dict.items(), key=operator.itemgetter(0))
    else:
        sorted_x = OrderedDict(sorted(sorted(_dict.items(), key=operator.itemgetter(0))))
    return sorted_x


def sort_dict_by_value(_dict, transpose=False):
    if transpose is False:
        sorted_x = sorted(_dict.items(), key=operator.itemgetter(1))
    else:
        sorted_x = OrderedDict(sorted(_dict.items(), key=operator.itemgetter(1)))
    return sorted_x
