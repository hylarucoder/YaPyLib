#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from yapylib.helpers.string.transpose import filter_chinese_characters, filter_all_chinese_things, filter_numbers, \
    shrink_repeated, get_digits_from_chinese, simple_render
from yapylib.helpers.string.utils import turn_full_to_half_width, turn_half_to_full_width

CHINESE_ARTICLE = """\
Python的创始人为吉多·范罗苏姆（Guido van Rossum）。1989年的圣诞节期间，
吉多·范罗苏姆为了在阿姆斯特丹打发时间，决心开发一个新的脚本解释程序，作为ABC语言的一种继承。
之所以选中Python作为程序的名字，是因为他是BBC电视剧——蒙提·派森的飞行马戏团
（Monty Python's Flying Circus）的爱好者。ABC是由吉多参加设计的一种教学语言。
就吉多本人看来，ABC这种语言非常优美和强大，是专门为非专业程序员设计的。
但是ABC语言并没有成功，究其原因，吉多认为是非开放造成的。
吉多决心在Python中避免这一错误，并获取了非常好的效果，完美结合了C和其他一些语言。[5]

就这样，Python在吉多手中诞生了。实际上，第一个实现是在Mac机上。
可以说，Python是从ABC发展起来，主要受到了Modula-3（另一种相当优美且强大的语言，为小型团体所设计的）的影响。
并且结合了Unix shell和C的习惯。

目前吉多仍然是Python的主要开发者，决定整个Python语言的发展方向。Python社区经常称呼他是仁慈的独裁者。

Python 2.0于2000年10月16日发布，增加了实现完整的垃圾回收，并且支持Unicode。

同时，整个开发过程更加透明，社区对开发进度的影响逐渐扩大。

Python 3.0于2008年12月3日发布，此版不完全兼容之前的Python源代码。
不过，很多新特性后来也被移植到旧的Python 2.6/2.7版本。

Python是完全面向对象的语言。函数、模块、数字、字符串都是对象。

并且完全支持继承、重载、派生、多重继承，有益于增强源代码的复用性。

Python支持重载运算符，因此Python也支持泛型设计。

相对于Lisp这种传统的函数式编程语言，Python对函数式设计只提供了有限的支持。
有两个标准库（functools, itertools）提供了与Haskell和Standard ML中类似的函数式程序设计工具。

虽然Python可能被粗略地分类为“脚本语言”（script language），
但实际上一些大规模软件开发项目例如Zope、Mnet及BitTorrent，Google也广泛地使用它。

Python的支持者较喜欢称它为一种高级动态编程语言，原因是“脚本语言”泛指仅作简单程序设计任务的语言，
如shell script、VBScript等只能处理简单任务的编程语言，并不能与Python相提并论。

Python本身被设计为可扩充的。并非所有的特性和功能都集成到语言核心。
Python提供了丰富的API和工具，以便程序员能够轻松地使用C、C++、Cython来编写扩充模块。
Python编译器本身也可以被集成到其它需要脚本语言的程序内。
因此，有很多人把Python作为一种“胶水语言”（glue language）使用。
使用Python将其他语言编写的程序进行集成和封装。
在Google内部的很多项目，例如Google App Engine使用C++编写性能要求极高的部分，
然后用Python或Java/Go调用相应的模块。[6]《Python技术手册》的作者马特利（Alex Martelli）
说：“这很难讲，不过，2004年，Python已在Google内部使用，Google召募许多Python高手，
但在这之前就已决定使用Python。他们的目的是尽量使用Python，在不得已时改用C++；
在操控硬件的场合使用C++，在快速开发时候使用Python。”[7]
"""

CHINESE_ARTICLE_CLEANED_ALL_CHINESE_TEXT = "Python·Guido" \
                                           "vanRossum1989·ABCPythonBBC·MontyPython" \
                                           "sFlyingCircusABCABCABCPythonC[5]PythonMacPy" \
                                           "thonABCModula3UnixshellCPythonPythonPythonPy" \
                                           "thon2020001016UnicodePython302008123Py" \
                                           "thonPython2627PythonPythonPythonLis" \
                                           "pPythonfunctoolsitertoolsHaskellSt" \
                                           "andardMLPythonscriptlanguageZo" \
                                           "peMnetBitTorrentGooglePythonsh" \
                                           "ellscriptVBScriptPythonPythonPyth" \
                                           "onAPICCCythonPythonPythongluela" \
                                           "nguagePythonGoogleGoogleAppEngi" \
                                           "neCPythonJavaGo[6]PythonAlexMartel" \
                                           "li2004PythonGoogleGooglePythonPy" \
                                           "thonPythonCCPython[7]"


@pytest.mark.parametrize('test_input,expected', [
    ("321323199509234453", "321323199509234453"),
    ("32132319中华人民共和国9509234453", "321323199509234453"),
])
def test_filter_chinese_characters(test_input, expected):
    assert filter_chinese_characters(test_input) == expected


@pytest.mark.parametrize('test_input,expected', [
    ("321323199509234453", "321323199509234453"),
    ("32132319中华人民共和国9509234453", "321323199509234453"),
    (CHINESE_ARTICLE, CHINESE_ARTICLE_CLEANED_ALL_CHINESE_TEXT),
])
def test_filter_all_chinese_things(test_input, expected):
    assert filter_all_chinese_things(test_input) == expected


@pytest.mark.parametrize('test_input,expected', [
    ("321323199509234453", ""),
    ("32132319中华人民共和国9509234453", "中华人民共和国"),
])
def test_filter_numbers(test_input, expected):
    assert filter_numbers(test_input) == expected


@pytest.mark.parametrize('test_input,expected', [
    ("321323199509234453", "321323199509234453"),
    ("32132319中华人民共和国9509234453", "32132319中华人民共和国9509234453"),
    ("３２１３２３１９中华人民共和国９５０９２３４４５３", "32132319中华人民共和国9509234453"),
    ("３２１３２３１９９５０９２３４４５３", "321323199509234453"),
])
def test_turn_full_to_half_width(test_input, expected):
    assert turn_full_to_half_width(test_input) == expected


@pytest.mark.parametrize('test_input,expected', [
    ("321323199509234453", "３２１３２３１９９５０９２３４４５３"),
    ("32132319中华人民共和国9509234453", "３２１３２３１９中华人民共和国９５０９２３４４５３"),
    ("３２１３２３１９中华人民共和国９５０９２３４４５３", "３２１３２３１９中华人民共和国９５０９２３４４５３"),
    ("３２１３２３１９９５０９２３４４５３", "３２１３２３１９９５０９２３４４５３"),
])
def test_turn_half_to_full_width(test_input, expected):
    assert turn_half_to_full_width(test_input) == expected


@pytest.mark.parametrize('test_input,max_times,expected', [
    ("asaaaaaaaaaaaaaaaas", 3, "asaaas"),
    ("asaaaaaaaaassssssss", 3, "asaaasss"),
    ("asaaaaaaaaassssssss", 5, "asaaaaasssss"),
])
def test_shrink_repeated(test_input, max_times, expected):
    assert shrink_repeated(test_input, max_times) == expected


@pytest.mark.parametrize('test_input,expected', [
    ('三千五百二十三', 3523),
    ('七十五亿八百零七万九千二百零八', 7508079208),
    ('四万三千五百二十一', 43521),
    ('三千五百二十一', 3521),
    ('三千五百零八', 3508),
    ('三五六零', 3560),
    ('一万零三十', 10030),
    ('', 0),
    ('零', 0),
    ('一', 1),
    ('二', 2),
    ('三', 3),
    ('四', 4),
    ('五', 5),
    ('六', 6),
    ('七', 7),
    ('八', 8),
    ('九', 9),
    ('十', 10),
    ('十一', 11),
    ('二十', 20),
    ('二十一', 21),
    ('一百', 100),
    ('一百零一', 101),
    ('一百一十', 110),
    ('一百二十三', 123),
    ('一千', 1000),
    ('一千零一', 1001),
    ('一千零一十', 1010),
    ('一千一百', 1100),
    ('一千零二十三', 1023),
    ('一千二百零三', 1203),
    ('一千二百三十', 1230),
    ('一万', 10000),
    ('一万零一', 10001),
    ('一万零一十', 10010),
    ('一万零一百', 10100),
    ('一万一千', 11000),
    ('一万零一十一', 10011),
    ('一万零一百零一', 10101),
    ('一万一千零一', 11001),
    ('一万零一百一十', 10110),
    ('一万一千零一十', 11010),
    ('一万一千一百', 11100),
    ('一万一千一百一十', 11110),
    ('一万一千一百零一', 11101),
    ('一万一千零一十一', 11011),
    ('一万零一百一十一', 10111),
    ('一万一千一百一十一', 11111),
    ('十万零二千三百四十五', 102345),
    ('十二万三千四百五十六', 123456),
    ('十万零三百五十六', 100356),
    ('十万零三千六百零九', 103609),
    ('一百二十三万四千五百六十七', 1234567),
    ('一百零一万零一百零一', 1010101),
    ('一百万零一', 1000001),
    ('一千一百二十三万四千五百六十七', 11234567),
    ('一千零一十一万零一百零一', 10110101),
    ('一千万零一', 10000001),
    ('一亿一千一百二十三万四千五百六十七', 111234567),
    ('一亿零一百零一万零一百零一', 101010101),
    ('一亿零一', 100000001),
    ('十一亿一千一百二十三万四千五百六十七', 1111234567),
    ('一百一十一亿一千一百二十三万四千五百六十七', 11111234567),
    ('一千一百一十一亿一千一百二十三万四千五百六十七', 111111234567),
    ('一万一千一百一十一亿一千一百二十三万四千五百六十七', 1111111234567),
    ('十一万一千一百一十一亿一千一百二十三万四千五百六十七', 11111111234567),
    ('一亿一千一百一十一万一千一百一十一亿一千一百二十三万四千五百六十七', 11111111111234567),
])
def test_get_digits_from_chinese(test_input, expected):
    assert get_digits_from_chinese(test_input) == expected


@pytest.mark.parametrize('test_input, context, expected', [
    ("{{{{ {{var}}", {"var": "replacement"}, "{{ replacement"),
])
def test_simple_render(test_input, context, expected):
    assert simple_render(test_input, context) == expected
