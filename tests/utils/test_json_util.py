import pytest
from yapylib.helpers.type_utils import is_json


@pytest.mark.parametrize('test_str,expected', [
    ("     ", False),
    ('{}', True),
    ('{asdf}', False),
    ('{"age":100}', True),
    ('{\'age\':100 }', False),
    ('{"age":100 }', True),
])
def test_is_json(test_str, expected):
    assert is_json(_str=test_str) == expected
