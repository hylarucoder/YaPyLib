# coding=utf-8
import time
import queue
from yapylib.concurrent.thread_pool import SimpleThreadPool

STOP_FLAG = object()


def test_simple_thread_pool():
    pre_q = queue.Queue()
    post_q = queue.Queue()
    for i in range(100):
        pre_q.put(i)

    pre_q.put(STOP_FLAG)

    def pre_process_item_func(in_q, out_q):
        while True:
            in_item = in_q.get()
            if in_item is STOP_FLAG:
                in_q.put(in_item)
                break
            time.sleep(0.3)
            print('in_item', in_item)
            out_q.put(in_item)
        print("<== 生产者: pre_process_item_func 就这样被你征服 切断了所有退路")

    def post_process_item_func(out_q):
        while True:
            try:
                out_item = out_q.get(timeout=10)
                time.sleep(0.3)
                print('out_item', out_item)
            except Exception() as e:
                print(e)
                break
        print("<== 消费者: post_process_item_func 我的剧情已落幕 我的爱恨已入土")

    # SimpleThreadPool().register(
    #     pre_process_item_func,
    #     pre_q,
    #     post_process_item_func,
    #     post_q).start()
