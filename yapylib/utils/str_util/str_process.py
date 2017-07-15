# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
字符串处理程序
1. 删除,替换,查找
2. 盘古化 https://github.com/hotoo/pangu.vim
3. 抽取html
4. 抽取json

@Author: twocucao
@Email: twocucao@gmail.com
@Date: 2016-09-19
@Desc: 针对其他的一些中文字符和英文字符,以及混合中英文字符进行一些简单的提取操作.

"""
import re

from yapylib.utils.str_util import PT_CHINESE_AND_NUMBER, PT_CHINESE_SETENCE
from yapylib.utils.str_util.str_validator import is_empty

import re
import string


class SimpleTemplate(string.Template):
    """
    origin: https://pymotw.com/3/string/index.html
    """
    delimiter = '{{'
    pattern = r'''
    \{\{(?:
    (?P<escaped>\{\{)|
    (?P<named>[_a-z][_a-z0-9]*)\}\}|
    (?P<braced>[_a-z][_a-z0-9]*)\}\}|
    (?P<invalid>)
    )
    '''


def simple_render(content, context):
    """
    :param content: 
    :param context: 
    :return: 
    print('MATCHES:', t.pattern.findall(t.template))
    print('SUBSTITUTED:', t.safe_substitute(var='replacement'))
    """
    t = SimpleTemplate(content)
    return t.safe_substitute(context)


def safe_sub(_str, dict):
    raise NotImplementedError()


def extract_pure_chinese(_str, keep_punctuaction=False):
    if keep_punctuaction:
        # TODO先这么写,以后再说
        return "".join(re.findall(PT_CHINESE_AND_NUMBER, _str))
    else:
        return "".join(re.findall(PT_CHINESE_AND_NUMBER, _str))


def squashing_danmuku(_str):
    if isinstance(_str, str):
        _str = _str.strip()
        return _str
    else:
        return None


def filter_chinese_characters(_str):
    new_str = re.sub(PT_CHINESE_SETENCE, "", _str)
    return new_str


def filter_chinese_punctuations(_str):
    new_str = re.sub(r"[\s+.!/_,$%^*(\"']+|[+—！，。？、~@#￥%…&*（）：；《》“”()»〔〕-]+", "", _str)
    return new_str


def filter_all_chinese_things(_str):
    new_str = filter_chinese_punctuations(filter_chinese_characters(_str))
    return new_str


def filter_numbers(_str):
    new_str = re.sub(r"\d+", "", _str)
    return new_str


def filter_english_characters(_str):
    raise NotImplementedError()


ch_puncs = ["！", "，", "。", "？", "、", "（", "）", "：", "；", "《", "》", "“ ", "” "]
en_puncs = ["!", ",", ".", "?", ",", "(", ")", ":", ";", "<", ">", "\"", "\""]


def sub_chinese_punctuations(_str):
    """
    :param _str:
    :return:
    """
    for k, v in zip(ch_puncs, en_puncs):
        _str = _str.replace(k, v)
    return _str


def shrink_repeated(_str, max_times=3):
    """
    :param _str:
    :param max_times:
    将重复 max_times 次以上的 字符串删减为 max_times 次
    :return:
    """
    pat = r'(.)\1{%d,}' % max_times
    repl = r''.join([r'\1' for i in range(max_times)])
    return re.sub(pat, repl, _str)


def shrink_online_rent(_str):
    _str = sub_chinese_punctuations(_str)
    _str = shrink_repeated(_str, 4)
    return _str


HALF2FULL = dict((i, i + 0xFEE0) for i in range(0x21, 0x7F))
HALF2FULL[0x20] = 0x3000

FULL2HALF = dict((i + 0xFEE0, i) for i in range(0x21, 0x7F))
FULL2HALF[0x3000] = 0x20


def turn_full_to_half_width(_str):
    '''
    Convert all ASCII characters to the full-width counterpart.
    '''
    return str(_str).translate(FULL2HALF)


def turn_half_to_full_width(_str):
    '''
    Convert full-width characters to ASCII counterpart
    '''
    return str(_str).translate(HALF2FULL)


"""
这是对HTML文本处理的一些常见的方案,主要是通过BeautifulSoup实现,主要用户处理常见的一些HTML处理和提取.
"""


def html_escape_chars_to_string(_str):
    return _str if is_empty(_str) else _str.replace("&lt;", "<") \
        .replace("&gt;", ">").replace("&amp;", "&").replace("&quot;", "\"")


def extract_links_from_html(_str):
    raise NotImplementedError()
    return ""


def shrink_string(_str, strip_chars=None, nullable=True):
    """
    :param _str:
    :param nullable:
    :param strip_chars:
    :return:
    """
    if isinstance(_str, str):
        if strip_chars is None:
            return _str.strip()
        else:
            return _str.strip(strip_chars)
    if nullable:
        return None
    else:
        return ""


def restrip_or_none(_str, strips=" ", replaces=""):
    if isinstance(_str, str):
        _str = _str.strip(strips + " ").replace(replaces, "")
        if len(_str) == 0:
            return None
        return _str
    else:
        return None


def half_width_to_full_width(_str):
    raise NotImplementedError
    return _str


def full_width_to_half_width(_str):
    raise NotImplementedError
    return _str


chinese_digits_mapping = {u'零': 0, u'一': 1, u'二': 2, u'三': 3, u'四': 4, u'五': 5, u'六': 6, u'七': 7, u'八': 8, u'九': 9,
                          u'十': 10, u'百': 100,
                          u'千': 1000, u'万': 10000,
                          u'０': 0, u'１': 1, u'２': 2, u'３': 3, u'４': 4, u'５': 5, u'６': 6, u'７': 7, u'８': 8, u'９': 9,
                          u'壹': 1, u'贰': 2, u'叁': 3, u'肆': 4, u'伍': 5, u'陆': 6, u'柒': 7, u'捌': 8, u'玖': 9, u'拾': 10,
                          u'佰': 100,
                          u'仟': 1000, u'萬': 10000,
                          u'亿': 100000000}


def get_digits_from_chinese(a):
    """
    :param a:
    :return:
    author: binux(17175297.hk@gmail.com)
    modified by: twocucao
    """
    count = 0
    result = 0
    tmp = 0
    Billion = 0
    while count < len(a):
        tmpChr = a[count]
        # print(tmpChr)
        tmpNum = chinese_digits_mapping.get(tmpChr, None)
        # 如果等于1亿
        if tmpNum == 100000000:
            result += tmp
            result = result * tmpNum
            # 获得亿以上的数量，将其保存在中间变量Billion中并清空result
            Billion = Billion * 100000000 + result
            result = 0
            tmp = 0
        # 如果等于1万
        elif tmpNum == 10000:
            result += tmp
            result = result * tmpNum
            tmp = 0
        # 如果等于十或者百，千
        elif tmpNum >= 10:
            if tmp == 0:
                tmp = 1
            result += tmpNum * tmp
            tmp = 0
        # 如果是个位数
        elif tmpNum is not None:
            tmp = tmp * 10 + tmpNum
        count += 1
    result = result + tmp
    result = result + Billion
    return result
