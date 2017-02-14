import random

import requests
import time

"""
自带代理池的下载
1. 集成basefetcher的Fetcher需要定制它的过滤法则
2. 可开启redis的代理池用于作分布式代理与分布式url的分布
3. 可开启monodb的response缓存体系
"""

TIMEOUT = 5

PROXIES = [
]


def choice_proxy():
    if PROXIES:
        return random.choice(PROXIES + [''])
    return ''


choice_proxy_item = choice_proxy()
proxies = {
    'http': choice_proxy_item,
    'https': choice_proxy_item
}


def get_headers():
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    }
    return headers


s = requests.Session()


def fetch(url, retry=0):
    choice_proxy_item = choice_proxy()
    proxies = {
        'http': choice_proxy_item,
        'https': choice_proxy_item
    }
    s.headers = get_headers()
    try:
        res = s.get(url, timeout=TIMEOUT, proxies=proxies)
        return res
    except (requests.exceptions.RequestException,
            requests.exceptions.ProxyError):
        if retry <= 8:
            print("休息会")
            time.sleep(2)
            return fetch(url, retry=retry + 1)
            # raise
    except Exception:
        if retry <= 8:
            print("着重休息会")
            time.sleep(2)
            return fetch(url, retry=retry + 1)
