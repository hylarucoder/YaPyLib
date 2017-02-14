import pytest

from yapylib.utils.random_util import uuid, random_ua
from yapylib.utils.str_util.str_regex import is_uuid

def test_uuid():
    assert is_uuid(str(uuid()))

def test_random_ua():
    """
    无需测试
    """
    #assert is_uuid(str(random_ua()))
    pass
