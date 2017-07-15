import json

import click
import parsel
from yapylib.cli import pass_context
from yapylib.utils.nlp_utils.dnw_utils import dnw_4_normal
from yapylib.utils.type_util import is_html, is_json
from yapylib.wrapped.requests import session


@click.command('rename', short_help='rename files by expression')
@click.argument('pathname', required=True, type=click.STRING)
@click.argument('operate', required=True, type=click.STRING)
@pass_context
def cli(ctx, pathname, operate):
    """
    example:

     - yapylib rename '*.jpg' '[R#abc#cde]'
     - yapylib rename '*.jpg' '[N#1#2]_[YMD]_[hms]_[C#5]'


    1. 从文件名中替换

    [R#regex#repl] : 删除regex匹配的字符串,替换为repl, 符合python 正则语法

    2. 类似于TotalCMD的重命名

    [N#1#2] : 文件名,第几个字符到第几个字符,和Python的Slice一致

    [YMD] : 年月日 格式为当前时间 20170712

    [hms] : 时分秒 格式为当前时间 073500

    [C#5] : 计数器 [C#4] : 从左开始填充0至长度为4 , 数字仅支持1-9, 如果不填则取消

    """
    import os
    import glob
    baned_file_list = ['.DS_Store', 'Thumbs.db']
    target_file_list = glob.glob(pathname)
    files_num = len(target_file_list)
    ctx.log('正在对路径 {} 的 {} 个文件进行重命名'.format(target_file_list, files_num))
    count_padding_length = len(str(files_num)) + 1
    count = 1
    for before_name in sorted(target_file_list, key=lambda f: os.stat(f).st_mtime):
        if before_name in baned_file_list:
            continue
        else:
            extension = os.path.splitext(before_name)[1]
            after_name = "{count}{extension}".format(count=str(count).zfill(count_padding_length), extension=extension)
            print("{} \t --> \t {}".format(before_name, after_name))
            os.rename(before_name, after_name)
            count += 1
