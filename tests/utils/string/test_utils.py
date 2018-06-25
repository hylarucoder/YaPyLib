import pytest

from yapylib.helpers.string.utils import is_blank, is_empty, is_valid_string, valid_similarity


@pytest.mark.parametrize('test_str,expected', [
    ("321323199509234453", False),
    ("     i\n\r ", False),
    ("     ", True),
    ("\n", True),
    (None, True),
])
def test_is_blank(test_str, expected):
    assert is_blank(_str=test_str) == expected


@pytest.mark.parametrize('test_str,expected', [
    ("321323199509234453", False),
    ("     i\n\r ", False),
    ("     ", False),
    ("\n", False),
    ("", True),
    (None, True),
])
def test_is_empty(test_str, expected):
    assert is_empty(_str=test_str) == expected


@pytest.mark.parametrize('test_str,expected', [
    ("321323199509234453", True),
    ("     i\n\r ", True),
    ("     ", False),
    ("\n", False),
    ("", False),
    (None, False),
])
def test_is_valid_string(test_str, expected):
    assert is_valid_string(_str=test_str) == expected


@pytest.mark.parametrize('test_str1,test_str2,expected', [
    ("321323199509234453", "3213239509234", 5),
    ("中国人", "美国人", 1),
    ("逛吃生命苦短逛吃", "大不如大小吃我大喝", 9),
    ("逛吃逛吃", "大吃大喝", 3),
])
def test_valid_similarity(test_str1, test_str2, expected):
    assert valid_similarity(test_str1, test_str2) == expected
