"""
1. AbstractComplexProcessPool
2. SimpleProcessPool
"""
from concurrent.futures.process import ProcessPoolExecutor


class AbstractComplexProcessPool(ProcessPoolExecutor):
    pass


class SimpleProcessPool(AbstractComplexProcessPool):
    pass


class DataAnalysisProcessPool(AbstractComplexProcessPool):
    """
    1. 数据分析过程中需要
    """

    def map(self, fn, *iterables, timeout=None, chunksize=1):
        """
        :param fn:
        :param iterables:
        :param timeout:
        :param chunksize:
        :return:
        """
        return super().map(fn, *iterables, timeout=timeout, chunksize=chunksize)
