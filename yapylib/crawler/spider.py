import random
import traceback

import requests
import time

from yapylib.crawler.fetcher import CaptchaException
from yapylib.logging import get_logger
from yapylib.utils.date_util import cur_time



class BaseSpider(object):
    default_timeout = 10
    request_max_retry = 3
    latest_upd_proxy_time = cur_time()
    current_upd_proxy_time = cur_time()
    spider_name = "基层爬虫"
    default_headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:44.0) Gecko/20100101 Firefox/44.0"
    }
    allowed_status_codes = [301, 200]

    def __init__(self, name, headers=None, proxy_mode=0):
        self.spider_name = name
        self.proxy_mode = proxy_mode
