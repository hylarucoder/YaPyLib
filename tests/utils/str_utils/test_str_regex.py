#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from yapylib.utils.str_util import PT_CHINESE_ID_CARD, PT_CHINESE_MOB_NUM, PT_CHINESE_MONEY, PT_CHINESE_SETENCE, \
    PT_CHINESE_TELEPHONE
from yapylib.utils.str_util.str_regex import *


@pytest.mark.parametrize('test_pattern,test_input,expected', [
    (PT_CHINESE_ID_CARD, "321323199509234453", True),
    (PT_CHINESE_ID_CARD, "爱是321323199509234453爱上的离开", True),
    (PT_CHINESE_ID_CARD, "1321323199509234453", True),
    (PT_CHINESE_MOB_NUM, "15123232033", True),
    (PT_CHINESE_MOB_NUM, "115123232033", True),
    (PT_CHINESE_MONEY, "¥ 115123232033", True),
    (PT_CHINESE_MONEY, "¥115123232033", True),
    (PT_CHINESE_MONEY, "苏州臭豆腐¥ 115123 / 人", True),
    (PT_CHINESE_SETENCE, "中华人民共和国", True),
    (PT_CHINESE_SETENCE, "¥115123232033", False),
    (PT_CHINESE_TELEPHONE, "0528-22332222", True),
    (PT_CHINESE_TELEPHONE, "000528-332222", False),
])
def test_has_pattern(test_pattern, test_input, expected):
    assert has_pattern(test_input, test_pattern) == expected


@pytest.mark.parametrize('test_pattern,test_input,expected', [
    (PT_CHINESE_ID_CARD, "321323199509234453", True),
    (PT_CHINESE_ID_CARD, "爱是321323199509234453爱上的离开", False),
    (PT_CHINESE_ID_CARD, "1321323199509234453", True),
    (PT_CHINESE_MOB_NUM, "15123232033", True),
    (PT_CHINESE_MOB_NUM, "115123232033", False),
    (PT_CHINESE_MONEY, "¥ 115123232033", True),
    (PT_CHINESE_MONEY, "¥115123232033", True),
    (PT_CHINESE_MONEY, "苏州臭豆腐¥ 115123 / 人", False),
    (PT_CHINESE_SETENCE, "中华人民共和国", True),
    (PT_CHINESE_SETENCE, "¥115123232033", False),
    (PT_CHINESE_TELEPHONE, "0528-22332222", True),
    (PT_CHINESE_TELEPHONE, "000528-332222", False),
])
def test_match_pattern(test_pattern, test_input, expected):
    assert match_pattern(test_input, test_pattern) == expected


@pytest.mark.parametrize('test_input,expected', [
    ("321323199509234453", False),
    ("000528-332222", False),
    ("521e7bb0-d8d5-4f49-a5c2-fee1aaf9e8c4", True),
])
def test_is_uuid(test_input, expected):
    assert is_uuid(test_input) == expected


@pytest.mark.parametrize('test_input,expected', [
    ("321323199509234453", False),
    ("000528-332222", False),
    ("521e7bb0-d8d5-4f49-a5c2-fee1aaf9e8c4", True),
])
def test_has_uuid(test_input, expected):
    assert has_uuid(test_input) == expected


@pytest.mark.parametrize('test_input,expected', [
    ("321323199509234453", None),
    ("000528-332222", None),
    ("521e7bb0-d8d5-4f49-a5c2-fee1aaf9e8c4", "521e7bb0-d8d5-4f49-a5c2-fee1aaf9e8c4"),
])
def test_extract_first_uuid(test_input, expected):
    assert extract_first_uuid(test_input) == expected


@pytest.mark.parametrize('test_input,expected', [
    ("321323199509234453", None),
    ("000528-332222", None),
    (
            "521e7bb0-d8d5-4f49-a5c2-fee1aaf9e8c4521e7bb0-d8d5-4f49-a5c2-fee1aaf9e8c4521e7bb0-d8d5-4f49-a5c2-fee1aaf9e8c4521e7bb0-d8d5-4f49-a5c2-fee1aaf9e8c4",
            ['521e7bb0-d8d5-4f49-a5c2-fee1aaf9e8c4', '521e7bb0-d8d5-4f49-a5c2-fee1aaf9e8c4',
             '521e7bb0-d8d5-4f49-a5c2-fee1aaf9e8c4', '521e7bb0-d8d5-4f49-a5c2-fee1aaf9e8c4']),
    (
            "521e7bb0-d8d5-4f49-a5c2-fee1aaf9e8c4   521e7bb0-d8d5-4f49-a5c2-fee1aaf9e8c4   521e7bb0-d8d5-4f49-a5c2-fee1aaf9e8c4   aslakdj 521e7bb0-d8d5-4f49-a5c2-fee1aaf9e8c4",
            ['521e7bb0-d8d5-4f49-a5c2-fee1aaf9e8c4', '521e7bb0-d8d5-4f49-a5c2-fee1aaf9e8c4',
             '521e7bb0-d8d5-4f49-a5c2-fee1aaf9e8c4', '521e7bb0-d8d5-4f49-a5c2-fee1aaf9e8c4']),
])
def test_extract_all_uuid(test_input, expected):
    assert extract_all_uuid(test_input) == expected


@pytest.mark.parametrize('test_input,expected', [
    ("1518333388", False),
    ("15183333888", True),
    ("1518333388815183333888 151833338881518333388815183333888", True)
])
def test_has_chinese_mob_num(test_input, expected):
    assert has_chinese_mob_num(test_input) == expected


@pytest.mark.parametrize('test_input,expected', [
    ("1518333388", None),
    ("15183333888", ["15183333888"]),
    ("1518333388815183333888 151833338881518333388815183333888",
     ['15183333888', '15183333888', '15183333888', '15183333888', '15183333888']),
])
def test_extract_all_chinese_mob_num(test_input, expected):
    assert extract_all_chinese_mob_num(test_input) == expected


@pytest.mark.parametrize('test_input,expected', [
    ("1518333388", False),
    ("15183333888", True),
])
def test_is_chinese_mob_num(test_input, expected):
    assert is_chinese_mob_num(test_input) == expected


@pytest.mark.parametrize('test_input,expected', [
    ("1518333388", True),
    ("plumbing fixtures 管道装置15183333888", True),
    ("mvenpå˙∆©©˚©˚©˚˙˚ick管道装置15183333888", True),
])
def test_is_clean_words(test_input, expected):
    assert is_clean_words(test_input) == expected
