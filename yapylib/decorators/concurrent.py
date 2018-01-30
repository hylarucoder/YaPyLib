import multiprocessing as mp

import time
from functools import wraps


def join_processing(func):
    """
    将任务放到进程里执行并阻塞当前进程,最后返回结果
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        def processing(*_args, **_kwargs):
            _q = _kwargs.pop('queue')
            _func = _kwargs.pop('func')
            start = time.time()
            _result = _func(*_args, **_kwargs)
            end = time.time()
            print(func.__name__, end - start)
            _q.put(_result)

        q = mp.Queue()
        kwargs['queue'] = q
        kwargs['func'] = func
        p = mp.Process(target=processing, args=args, kwargs=kwargs)
        p.start()
        result = q.get()
        p.join()
        return result

    return wrapper
