from concurrent.futures import ThreadPoolExecutor
import threading
import time

"""
1. AbstractComplexThreadPool
2. SimpleThreadPool
"""
MAX_WORKERS_NUM = 10
MAX_PRE_PROCESS_WORKER_NUM = 6
MAX_POST_PROCESS_WORKER_NUM = 3


class AbstractComplexThreadPool(object):
    pass


class SimpleThreadPool(AbstractComplexThreadPool):
    """
    使用:
    第一步:注册
    第二步:启动
    """

    def monitoring(self):
        """
        监控线程,对队列进行简单的监控
        :returns: TODO
        """
        time_record = []

        while True:
            time.sleep(1)
            print("==>生产者队列", self.pre_process_queue.qsize())
            print("==>消费者队列", self.post_process_queue.qsize())

            time_record.append(self.post_process_queue.qsize())

            if len(time_record) > 30 and sum(time_record[-50:]):
                break
        print("<== 监控线程 monitoring 我的剧情已落幕 我的爱恨已入土")

    def register(self, pre_process_item_func, pre_process_queue, post_process_item_func, post_process_queue):
        """
        :pre_process_item_func:
        :pre_process_queue:
        :post_process_item_func:
        :post_process_queue:
        :returns: TODO
        """
        self.pre_process_item_func = pre_process_item_func
        self.pre_process_queue = pre_process_queue
        self.post_process_item_func = post_process_item_func
        self.post_process_queue = post_process_queue
        return self

    def start(self):
        """
        运行脚本
        :returns: TODO
        """
        self.pool = ThreadPoolExecutor(MAX_WORKERS_NUM)
        for i in range(MAX_PRE_PROCESS_WORKER_NUM):
            self.pool.submit(self.pre_process_item_func, self.pre_process_queue, self.post_process_queue)
        for i in range(MAX_POST_PROCESS_WORKER_NUM):
            self.pool.submit(self.post_process_item_func, self.post_process_queue)
        self.pool.submit(self.monitoring)

    pass
