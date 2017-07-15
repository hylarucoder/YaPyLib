"""
string_util 主要处理 比较短的文本,长文本的处理交给text_util

对字符串的一些常见的判断.

1. is_blank 为None或者strip以后为0
2. is_empty 为None或者长度为0
3. has?
4. 返回字符串特点
提取请求url中的中文内容.

"""
import re

from yapylib.utils.str_util import PT_UUID


def is_blank(_str):
    """
    判断是否为空(除去空格换行)
    :param _str:
    :return:
    """
    return _str is None or len(_str.strip()) == 0


def is_empty(_str):
    """
    判断是否为空(包含空格字符)
    :param _str:
    :return:
    """
    return _str is None or len(_str) == 0


def is_valid_string(_str):
    return isinstance(_str, str) and _str.strip() != ''


def is_equal(actual, expected):
    '''
    :param _str:
    :return:
    '''
    return actual == expected


def contains_chinese(content):
    pass


def valid_realname(content):
    pass


def valid_phone_num(content):
    pass


def valid_account(content):
    pass


def valid_simple_password(content):
    pass


def valid_complex_password(content):
    pass


def valid_email(content):
    pass


def valid_ip(content):
    pass


def valid_uuid(content):
    pass


def valid_url(content):
    pass


def valid_vehicle_num(content):
    pass


def LevenshteinDistance(s, t):
    '''字符串相似度算法（Levenshtein Distance算法）

  一个字符串可以通过增加一个字符，删除一个字符，替换一个字符得到另外一个
  字符串，假设，我们把从字符串A转换成字符串B，前面3种操作所执行的最少
  次数称为AB相似度
  这算法是由俄国科学家Levenshtein提出的。
  Step Description
  1 Set n to be the length of s.
    Set m to be the length of t.
    If n = 0, return m and exit.
    If m = 0, return n and exit.
    Construct a matrix containing 0..m rows and 0..n columns.
  2 Initialize the first row to 0..n.
    Initialize the first column to 0..m.
  3 Examine each character of s (i from 1 to n).
  4 Examine each character of t (j from 1 to m).
  5 If s[i] equals t[j], the cost is 0.
    If s[i] doesn't equal t[j], the cost is 1.
  6 Set cell d[i,j] of the matrix equal to the minimum of:
    a. The cell immediately above plus 1: d[i-1,j] + 1.
    b. The cell immediately to the left plus 1: d[i,j-1] + 1.
    c. The cell diagonally above and to the left plus the cost:
       d[i-1,j-1] + cost.
  7 After the iteration steps (3, 4, 5, 6) are complete, the distance is
    found in cell d[n,m]. '''

    m, n = len(s), len(t)
    if not (m and n):
        return m or n

    # 构造矩阵
    matrix = [[0 for i in range(n + 1)] for j in range(m + 1)]
    matrix[0] = list(range(n + 1))
    for i in range(m + 1):
        matrix[i][0] = i

    for i in range(m):
        for j in range(n):
            cost = int(s[i] != t[j])
            # 因为 Python 的字符索引从 0 开始
            matrix[i + 1][j + 1] = min(
                matrix[i][j + 1] + 1,  # a.
                matrix[i + 1][j] + 1,  # b.
                matrix[i][j] + cost  # c.
            )

    return matrix[m][n]


valid_similarity = LevenshteinDistance
