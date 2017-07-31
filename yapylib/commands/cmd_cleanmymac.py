import click
import pytest
import shutil

from yapylib.cli import pass_context
from yapylib.utils import file_utils


@click.command('cleanmymac', short_help='Software Like Clean My Mac')
@pass_context
def cli(ctx):
    """
    依照YML文件中的地址进行缓存文件的清理,如果没有,则
    """
    ctx.log('正在测试')
    before_disk_usage = shutil.disk_usage(".")
    dirs = [
        "/Volumes/*/.Trashes"
    ]
    for _dir in dirs:
        fs = file_utils.get_folder_size(_dir)
        print("路径\t{_dir}\t{fs}".format(_dir=_dir, fs=fs))
        file_utils.delete_file(_dir)
        fs = file_utils.get_folder_size(_dir)
        print("路径\t{_dir}\t{fs}".format(_dir=_dir, fs=fs))
    after_disk_usage = shutil.disk_usage(".")
