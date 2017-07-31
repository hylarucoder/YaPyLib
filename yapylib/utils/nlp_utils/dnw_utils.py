import re
from collections import Counter

import numpy as np
import pandas as pd
from numpy import log
from yapylib.utils.str_util.str_process import shrink_online_rent


def dnw_4_normal(input_text):
    """
    源代码基于 http://spaces.ac.cn/archives/3491/
    原理基于 http://www.matrix67.com/blog/archives/5044
    :param input_text:
    :return:
    """
    # 定义要去掉的标点字
    drop_dict = [u'，', u'\n', u'。', u'、', u'：', u'(', u')', u'[', u']', u'.', u',', u' ', u'\u3000', u'”', u'“', u'？',
                 u'?',
                 u'！', u'‘', u'’', u'…']
    for i in drop_dict:  # 去掉标点字
        input_text = input_text.replace(i, '')

    min_count = 2  # 录取词语最小出现次数
    min_support = 4  # 录取词语最低支持度，1代表着随机组合
    min_s = 2  # 录取词语最低信息熵，越大说明越有可能独立成词
    max_sep = 10  # 候选词语的最大字数

    # 为了方便调用，自定义了一个正则表达式的词典
    regexes = {}
    for i in range(2, max_sep + 1):
        k = i
        v = '(' + '.' * i + ')'
        regexes[k] = v

    t = [pd.Series(list(input_text)).value_counts()]  # 保存结果用。

    tsum = t[0].sum()  # 统计总字数
    rt = []  # 保存结果用

    for m in range(2, max_sep + 1):
        print(u'正在生成%s字词...' % m)
        t.append([])
        for i in range(m):  # 生成所有可能的m字词
            t[m - 1] = t[m - 1] + re.findall(regexes[m], input_text[i:])

        t[m - 1] = pd.Series(t[m - 1]).value_counts()  # 逐词统计
        t[m - 1] = t[m - 1][t[m - 1] > min_count]  # 最小次数筛选
        tt = t[m - 1][:]
        for k in range(m - 1):
            qq = np.array(list(map(lambda ms: tsum * t[m - 1][ms] / t[m - 2 - k][ms[:m - 1 - k]] / t[k][ms[m - 1 - k:]],
                                   tt.index))) > min_support  # 最小支持度筛选。
            tt = tt[qq]
        rt.append(tt.index)

    def cal_S(sl):  # 信息熵计算函数
        return -((sl / sl.sum()).apply(log) * sl / sl.sum()).sum()

    for i in range(2, max_sep + 1):
        print(u'正在进行%s字词的最大熵筛选(%s)...' % (i, len(rt[i - 2])))
        pp = []  # 保存所有的左右邻结果
        for j in range(i):
            pp = pp + re.findall('(.)%s(.)' % regexes[i], input_text[j:])
        pp = pd.DataFrame(pp).set_index(1).sort_index()  # 先排序，这个很重要，可以加快检索速度
        index = np.sort(np.intersect1d(rt[i - 2], pp.index))  # 作交集
        # 下面两句分别是左邻和右邻信息熵筛选
        index = index[np.array(list(map(lambda s: cal_S(pd.Series(pp[0][s]).value_counts()), index))) > min_s]
        rt[i - 2] = index[np.array(list(map(lambda s: cal_S(pd.Series(pp[2][s]).value_counts()), index))) > min_s]

    # 下面都是输出前处理
    for i in range(len(rt)):
        t[i + 1] = t[i + 1][rt[i]]
        t[i + 1].sort(ascending=False)

    # 保存结果并输出
    return pd.DataFrame(pd.concat(t[1:]))


def dnw_4_core(input_texts):
    """
    :param input_texts:
    :return:

    统计指定长度的候选词 频数,左邻字信息熵 , 右邻字信息熵
    参考链接实现: https://github.com/izisong/new-words-discovery
    """

    unrecord_word_length_min = 2
    unrecord_word_length_max = 10

    # Step 1. 指定登陆词长度范围,计算词频
    freq = Counter()
    cur_text = input_texts
    for cur_len in range(unrecord_word_length_min, unrecord_word_length_max + 1):
        # 依次登录登陆词为cur_len的词
        cur_text_len = len(cur_text)
        cur_words = [cur_text[i:i + cur_len] for i in range(0, cur_text_len - cur_len)]
        freq.update(cur_words)

    # Step 2. 过滤掉
    # Step 3. 指定登录城市

    # Step 1


def dnw_4_bilibili(input_text):
    """
    针对Bilibili弹幕的新词发现算法
    :param input_text:
    :return:
    """

    # 预处理, 去掉中文符号,应该没有人拿中文符号表情吧
    input_text = shrink_online_rent(input_text)
    return dnw_4_normal(input_text)

    pass


def dnw_4_danmuku(input_text, output):
    """
    针对弹幕的新词发现算法
    :param input_text:
    :return:
    """
    pass


def dnw_4_netcomment(input_text, output):
    """
    针对网络评论的新词发现算法
    :param input_text:
    :return:
    """
    pass
