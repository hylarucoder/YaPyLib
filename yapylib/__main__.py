import click

from yapylib.logging import get_logger
from yapylib.utils.http_utils import download_with_progress
from yapylib.utils.macos_util import notify
from yapylib.utils.sys_utils import check_setting_and_env


@click.command()
def main():
    """
    main function
    1. 监测环境,并且完成项目的初始化 (1. Py基本环境 ; 2. 数据库 3. 环境)
    2.
    """
    get_logger("project").info("初始化基本运行环境....正在检测环境....")
    check_setting_and_env()

    download_with_progress(
        "http://101.44.1.119/files/2043000006744998/down10.zol.com.cn/zhuyeliulan/57.0.2987.74_chrome_installer.exe",
        "/Users/twocucao/Downloads/chrome.exe")
    notify("YaPyLib下载完毕", "精选美女小视频", "本条消息自带响声", sound=True)


if __name__ == '__main__':
    main()
