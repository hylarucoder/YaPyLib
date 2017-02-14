"""
因为总是涉及到到判断分类,大分类,中分类,小分类,细分分类这些树形结构的东西,所以写这个模块进行判断
"""


def get_level(*var_arr):
    """
    :param vars: 
    :return: 
    [None,None,1] -> 3
    [1,1,1] -> 3
    [1,1,None] -> 2
    """
    level = -1
    for index, var in enumerate(var_arr):
        if var is not None:
            level = index + 1
    return level
