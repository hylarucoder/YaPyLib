import time
import traceback

import requests

from yapylib.logging import get_logger


class FetchWorker(object):
    """
    """

    def __init__(self, spider, proxy_mode=0):
        self.spider = spider
        self._session = requests.Session()
        self._session.headers = self.spider.default_headers
        self.default_timeout = 10
        self.max_retry = 4
        self.use_online_proxy = True
        self.allowed_parsed_status_codes = {200}

    def get_fetching(self):
        pass

    def post_fetching(self):
        pass

    def fetch(self, url, params=None, retry=0, func=None, sleep_time=2):
        proxy = self._get_requests_proxies()
        try:
            get_logger().info("使用代理IP {}".format(proxy))
            res = self._session.get(url, timeout=self.default_timeout, proxies=proxy)
            if hasattr(res, 'encoding'):
                res.encoding = 'utf-8'
            if func and hasattr(res, "status_code"):
                # TODO: 这里可能需要验证一下数据
                if self.parse_status_code(res.status_code):
                    # 请求成功
                    if func and hasattr(res, "text"):
                        func(res.text)
                    return res
                else:
                    # 是否满足
                    return self.fetch(url, params, retry, func, sleep_time)
        except (requests.exceptions.RequestException, requests.exceptions.ProxyError) as e:
            get_logger().info("请求异常或者代理连接错误 {}".format(e))
            if retry <= self.max_retry:
                if sleep_time:
                    time.sleep(sleep_time)
                return self.fetch(url, params, retry, func, sleep_time)
        except requests.exceptions.ReadTimeout as e:
            get_logger().info("请求超时 {}".format(e))
            if retry <= self.max_retry:
                if sleep_time:
                    time.sleep(sleep_time)
                return self.fetch(url, params, retry, func, sleep_time)
        except CaptchaException as e:
            get_logger().info("需要验证码 - 代理为{} ".format(proxy))
        except Exception as e:
            get_logger().info("其他问题{}".format(e))
            traceback.print_exc()
            if retry <= self.max_retry:
                if sleep_time:
                    time.sleep(sleep_time)
                return self.fetch(url, params, retry, func, sleep_time)

    def _random_online_proxy(self):
        return ""

    def _get_requests_proxies(self):
        """
        为了省事,直接用的是阿布云
        :return:
        """
        if self.use_online_proxy:
            choice_proxy_item = self._random_online_proxy()
        else:
            choice_proxy_item = self._random_stable_proxy()
        return {
            'http': "http://" + choice_proxy_item.replace("http://", ""),
            'https': "https://" + choice_proxy_item.replace("https://", "")
        }

    def parse_status_code(self, status_code):
        status_code = int(status_code)
        if int(status_code) in self.allowed_parsed_status_codes:
            return True
        elif status_code == 407:
            get_logger().error("需要代理进行认证")
            return False
        elif status_code >= 500:
            get_logger().error("对方服务器故障")
            return False
        else:
            get_logger().error("需要代理进行认证")
            return False

    pass


class CaptchaException(Exception):
    pass
