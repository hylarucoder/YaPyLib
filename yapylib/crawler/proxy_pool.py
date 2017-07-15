import random

from yapylib.utils.date_util import cur_time

NO_PROXY = 0
ONLINE_PROXY = 1
STABLE_PROXY = 2
PRIVATE_PROXY = 3


class ProxyPool(object):
    """
    用于挑选代理池,三种类型的代理:
    稳定代理
    不稳定代理
    私密代理
    定期更新代理,否则直接退出
    """
    stable_proxies = []  # 在线的稳定的API
    online_proxies = []  # 在线的不稳定的代理API
    private_proxies = []  # 在线的不稳定的代理API

    def __init__(self, mode=0):

        pass

    def choice_proxy(self):

        pass

    def _random_stable_proxy(self):
        if self.stable_proxies:
            if self.use_local:
                return random.choice(self.stable_proxies + [""])
            return random.choice(self.stable_proxies)
        return ''

    def _random_online_proxy(self):
        """
        :return:
        使用一分钟后,自动获取并且更新
        """
        self.current_time = cur_time()

        last_period = self.current_time - self.lastest_time

        if last_period > 60 or len(self.online_proxies) == 0:
            url = "http://dev.kuaidaili.com/api/getproxy/?orderid=xxx"
            self.online_proxies = requests.get(url).text.split("\r\n")
            print(self.online_proxies)
            self.lastest_time = self.current_time
        return random.choice(self.online_proxies)
