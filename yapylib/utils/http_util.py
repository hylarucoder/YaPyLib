import random

import click
import requests
import time

"""
自带代理池的下载
1. 集成basefetcher的Fetcher需要定制它的过滤法则
2. 可开启redis的代理池用于作分布式代理与分布式url的分布
3. 可开启monodb的response缓存体系
"""

CHUNK_SIZE = 40960

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


def choice_ol_proxy():
    global last_time
    global ol_proxies
    now = time.time()
    print("last_time -->", last_time)
    print("now -> ", now)

    if ((now - last_time) // 60) > 2 or len(ol_proxies) < 10:
        url = "http://dps.kuaidaili.com/api/getdps/?orderid=949207348447570&num=50&ut=1&sep=1"
        while True:
            try:
                ol_proxies = requests.get(url).text.split("\r\n")

                print(ol_proxies)
                if len(ol_proxies) > 10:
                    break
            except Exception:
                pass
        last_time = now
    return random.choice(ol_proxies)


s = requests.Session()


def fetch(url, retry=0, func=None):
    choice_proxy_item = choice_ol_proxy()
    proxies = {
        # 'http': choice_proxy_item,
        'https': choice_proxy_item
    }
    # print(proxies)
    # s.headers = get_headers()
    # s.headers.update({'user-agent': get_user_agent()})
    try:
        res = s.get(url, timeout=TIMEOUT, proxies=proxies)
        # print(res.status_code)
        res.encoding = 'utf-8'
        if func:
            if func(res.text):
                pass
            else:
                raise Exception
        return res
    except (requests.exceptions.RequestException,
            requests.exceptions.ProxyError):
        if retry <= 8:
            # print("休息会")
            time.sleep(2)
            return fetch(url, retry=retry + 1, func=func)
            # raise
    except Exception:
        if retry <= 8:
            # print("着重休息会")
            time.sleep(2)
            return fetch(url, retry=retry + 1, func=func)


def download_with_progress(url, file_name, session=None):
    if session:
        response = session.get(url, stream=True)
    else:
        response = requests.get(url, stream=True)
    total_length = response.headers.get('content-length')
    with open(file_name, "wb") as f:
        try:
            total_length = int(total_length)
        except Exception:
            total_length = 1000
        with click.progressbar(length=total_length, label='Downloading file', show_percent=True) as bar:
            if total_length is None:  # no content length header
                f.write(response.content)
            else:
                dl = 0
                for data in response.iter_content(chunk_size=CHUNK_SIZE):
                    dl += len(data)
                    f.write(data)
                    bar.update(len(data))
