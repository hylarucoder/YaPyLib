from yapylib.helpers.tree_util import get_level


def test_get_level_obj():
    obj1 = None
    obj2 = None
    obj3 = None
    obj4 = 1
    assert get_level(obj1, obj2, obj3, obj4) == 4
    obj1 = None
    obj2 = None
    obj3 = 1
    obj4 = 1
    assert get_level(obj1, obj2, obj3, obj4) == 4
    obj1 = None
    obj2 = 1
    obj3 = None
    obj4 = 1
    assert get_level(obj1, obj2, obj3, obj4) == 4
    obj1 = None
    obj2 = 1
    obj3 = 1
    obj4 = None
    assert get_level(obj1, obj2, obj3, obj4) == 3
