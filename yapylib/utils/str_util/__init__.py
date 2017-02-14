"""
包含如下的工具:
1. 字符串抽取工具类: 提取字符串
2. 字符串校验工具类: 校验字符串
3. 字符串处理工具类: 处理字符串

处理范围为:

1. 网页
2. 中文/英文
3. 货币
4. 其他
"""
import re

"""
@Author: twocucao
@Email: twocucao@gmail.com
@Date: 2016-09-19
@Desc: 常用正则表达式,用于抽取/验证/替换

是整数? 是小数? 是QQ? 是日期? 是链接? 是IP? 银行卡? 电子邮箱? 其他

参考实现:
https://github.com/madisonmay/CommonRegex/blob/master/commonregex.py
http://blog.jobbole.com/96052/

"""

PT_CHINESE = '([\u4e00-\u9fa5]+)+?'
PT_CHINESE_AND_NUMBER = '([\u4e00-\u9fa5\d\w]+)+?'
PT_CLEAN_WORDS = '([\u4e00-\u9fa5\d\s\a\w]+)+?'
PT_CHINESE_ID_CARD = r"([0-9]){7,18}(x|X)?"
PT_CHINESE_MOB_NUM = r"(?:13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}"
PT_CHINESE_TELEPHONE = r"\d{3}-\d{8}|\d{4}-\d{7}"
PT_CHINESE_MONEY = r"¥\s*\d+"
PT_CHINESE_PRICE = r'[$]\s?[+-]?[0-9]{1,3}(?:(?:,?[0-9]{3}))*(?:\.[0-9]{1,2})?'
PT_CHINESE_SETENCE = r"[\u4e00-\u9fa5]{1,}"
PT_DATE = r''
PT_DATETIME = r""
PT_DOMAIN = r"[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(/.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+/.?"
PT_EMAIL = r"([a-z0-9!#$%&'*+\/=?^_`{|.}~-]+@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"
PT_HEX_COLOR = r'(#(?:[0-9a-fA-F]{8})|#(?:[0-9a-fA-F]{3}){1,2})\\b'
PT_HTTP_HTTPS_LINK = r""
PT_INT_NUM = r"[0-9]*"
PT_IP_V4 = r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
PT_IP_V6 = r'\s*(?!.*::.*::)(?:(?!:)|:(?=:))(?:[0-9a-f]{0,4}(?:(?<=::)|(?<!::):)){6}(?:[0-9a-f]{0,4}(?:(?<=::)|(?<!::):)[0-9a-f]{0,4}(?:(?<=::)|(?<!:)|(?<=:)(?<!::):)|(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]?\d)(?:\.(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]?\d)){3})\s*'
PT_PREFERED_DATE = r"\d{4}-\d{1,2}-\d{1,2}"
PT_PREFERED_DATE_TIME = r""
PT_TIME = r""
PT_QQ_NUM = r"[1-9][0-9]{4,}"
PT_UUID = r'[a-f\d]{8}-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{12}'

REGEXES = {
    'uuid': PT_UUID,
    'clean_words': PT_CLEAN_WORDS,
    'chinese': PT_CHINESE,
    'chinese_id_card': PT_CHINESE_ID_CARD,
    'chinese_and_num': PT_CHINESE_AND_NUMBER,
    'chinese_mob_num': PT_CHINESE_MOB_NUM,
    'chinese_telephone': PT_CHINESE_TELEPHONE,
    'chinese_money': PT_CHINESE_MONEY,
    'ipv4': PT_IP_V4,
    'ipv6': PT_IP_V6,
    'date': PT_DATE,
    'time': PT_TIME,
    'qq_num': PT_QQ_NUM,
    'email': PT_EMAIL,
    'link': PT_HTTP_HTTPS_LINK,
    'datetime': PT_DATETIME,
}
