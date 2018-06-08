# coding=utf-8
import time
from yapylib.profile.ptime import timethis


@timethis
def net_fetch_xxxx():
    print("假装我是net_fetch")
    time.sleep(3)


def test_timethis():
    net_fetch_xxxx()
