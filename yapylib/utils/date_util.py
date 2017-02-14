import datetime
import time


def cur_time():
    return time.time()


def fmt_cur_date_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def fmt_cur_date():
    return time.strftime('%Y-%m-%d', time.localtime(time.time()))


def fmt_cur_time():
    return time.strftime('%H:%M:%S', time.localtime(time.time()))


def get_date_range(start_str, end_str, day_interval):
    """
    不包含结束时间
    :param start_str:
    :param end_str:
    :param day_interval:
    :return:
    """
    start = datetime.datetime.strptime(start_str, "%Y-%m-%d")
    end = datetime.datetime.strptime(end_str, "%Y-%m-%d")
    date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days)]
    date_formated = [date_item.strftime("%Y-%m-%d") for date_item in date_generated]
    return date_formated


def get_date_from_str(date_str):
    """
    :param date_str:
    :return:
    """
    # TODO: 有机会看看一些库是怎么处理各种时间格式的
    return datetime.datetime.strptime(date_str, '%Y-%m-%d')
