import time
from functools import wraps

from yapylib.settings import DEBUG

NET_DICT = {
    "net_fetch_": "网络请求",
    "db_sel_": "数据库 查询",
    "db_upd_": "数据库 更新",
    "db_del_": "数据库 删除"
}


def timethis(func):
    """
    Decorator that reports the execution time.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:

        1. 定义操作

        net_fetch_  网络请求

        db_sel_     数据库 查询
        db_upd_     数据库 更新
        db_del_     数据库 删除

        """
        func_name = func.__name__
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        msg = "{func_name} :\t 耗时 {last_sec}".format(func_name=func_name, last_sec=(end - start))
        if DEBUG:
            for k, v in NET_DICT.items():
                if func_name.startswith(k):
                    msg = "{type_name} - \t {func_name} :\t 耗时 {last_sec}".format(type_name=v, func_name=func_name,
                                                                                  last_sec=(end - start))
                else:
                    msg = "{type_name} - \t {func_name} :\t 耗时 {last_sec}".format(type_name="未命名", func_name=func_name,
                                                                                  last_sec=(end - start))
        print(msg)

        return result

    return wrapper
