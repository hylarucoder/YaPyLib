import json
import shutil
import sys

import click
import click_completion
import crayons
import requests
from click_didyoumean import DYMCommandCollection

from yapylib.cmd.core import format_help
from yapylib.helpers import file
from yapylib.helpers.type_utils import is_html, is_json
from .__version__ import __version__

# from . import settings

click_completion.init()

CONTEXT_SETTINGS = dict(
    help_option_names=['-h', '--help'],
)


class YaPyLibGroup(click.Group):

    def get_help_option(self, ctx):
        help_options = self.get_help_option_names(ctx)

        def show_help(ctx, param, value):
            if value and not ctx.resilient_parsing:
                if not ctx.invoked_subcommand:
                    click.echo(format_help(ctx.get_help()))
                else:
                    click.echo(ctx.get_help(), color=ctx.color)
                ctx.exit()

        return click.Option(help_options,
                            is_flag=True,
                            is_eager=True,
                            expose_value=False,
                            callback=show_help,
                            help='Show this message and exit.',
                            )


def setup_verbose(ctx, param, value):
    if value:
        import logging
        logging.getLogger('requests').setLevel(logging.INFO)
    return value


@click.group(cls=YaPyLibGroup,
             invoke_without_command=True,
             context_settings=CONTEXT_SETTINGS,
             )
@click.option('-v', '--verbose', is_flag=True,
              help='Enables verbose mode.')
@click.version_option(
    prog_name=crayons.white('yapylib', bold=True), version=__version__
)
@click.pass_context
def cli(ctx, verbose):
    """
    The Must-Have Utils For Every Pythonista 2016 - 2018.
    """
    # ctx.verbose = verbose
    click.echo(format_help(ctx.get_help()))


@click.command(
    short_help="execute python and then enter ipython",
    context_settings=dict(ignore_unknown_options=True, allow_extra_args=True),
)
def run():
    click.echo("is executing")
    pass


@click.command(
    short_help="execute python and then enter ipython",
    context_settings=dict(ignore_unknown_options=True, allow_extra_args=True),
)
@click.argument('url', required=True, type=click.STRING)
@click.pass_context
def fetch(ctx, url):
    import parsel
    click.echo("is executing")
    """使用REQUESTS请求某个地址,跳转到IPython便于下一步解析."""
    ctx.log('正在请求网址 %s', url)
    from IPython import embed
    session = requests.session()
    res = session.get(url)
    # 验证码判断
    content = res.text
    response = parsel.Selector(content)
    # TODO: is_html 有错误
    if is_html(content):
        ctx.log('请求内容为HTML')
        response = parsel.Selector(content)
    elif is_json(content):
        ctx.log('请求内容为JSON')
        response = json.loads(content)
    else:
        ctx.log('请求内容为未知')
        pass

    embed()


@click.command(
    short_help="simple file server for transfer files with mac and other devices",
    context_settings=dict(ignore_unknown_options=True, allow_extra_args=True),
)
def file_server():
    click.echo("is serving file")
    pass


@click.command(
    short_help="simple download",
    context_settings=dict(ignore_unknown_options=True, allow_extra_args=True),
)
def download():
    click.echo("is downloading")
    pass


@click.command(
    short_help="complex rename and confirm with vim",
    context_settings=dict(ignore_unknown_options=True, allow_extra_args=True),
)
def discover_new_words():
    click.echo("discover new words")
    pass


@click.command(
    short_help="self testing",
    context_settings=dict(ignore_unknown_options=True, allow_extra_args=True),
)
def self_test():
    click.echo("is self test")
    """使用REQUESTS请求某个地址,跳转到IPython便于下一步解析."""
    all_colors = 'black', 'red', 'green', 'yellow', 'blue', 'magenta', \
                 'cyan', 'white'
    for color in all_colors:
        click.echo(click.style('I am colored %s' % color, fg=color))
    for color in all_colors:
        click.echo(click.style('I am colored %s and bold' % color,
                               fg=color, bold=True))
    for color in all_colors:
        click.echo(click.style('I am reverse colored %s' % color, fg=color,
                               reverse=True))

    click.echo(click.style('I am blinking', blink=True))
    click.echo(click.style('I am underlined', underline=True))
    args_str = ["-s"]
    import pytest
    pytest.cmdline.main(args_str)
    pass


@click.command(
    short_help="what the file?",
    context_settings=dict(ignore_unknown_options=True, allow_extra_args=True),
)
def wtf():
    click.echo("is self test")
    pass


"""
实用工具类
"""


@click.command(
    short_help="unzip 自动判断 是否为GBK 编码 然后正常解压",
    context_settings=dict(ignore_unknown_options=True, allow_extra_args=True),
)
@click.argument('file', required=True, type=click.STRING)
def unzip(file=None):
    click.echo("is unzipping gbk")
    from yapylib.helpers.file import unzip_gbk_file
    unzip_gbk_file(file, None)
    pass


@click.command(
    short_help="rename 和TotalCMD相同的重命名神器，最后可在 vim 中预览结果",
    context_settings=dict(ignore_unknown_options=True, allow_extra_args=True),
)
def rename():
    click.echo("is unzipping gbk")
    pass


@click.command(
    short_help="unzip gbk package",
    context_settings=dict(ignore_unknown_options=True, allow_extra_args=True),
)
def clean():
    click.echo("is unzipping gbk")
    pass


@click.command(
    short_help="self testing",
    context_settings=dict(ignore_unknown_options=True, allow_extra_args=True),
)
def summary():
    click.echo("is self test")
    pass


@click.command(
    short_help="Software Like Clean My Mac",
    context_settings=dict(ignore_unknown_options=True, allow_extra_args=True),
)
def cleanmymac():
    """
    我怎么知道
    """
    before_disk_usage = shutil.disk_usage(".")
    dirs = [
        "/Volumes/*/.Trashes"
    ]
    for _dir in dirs:
        fs = file.get_folder_size(_dir)
        print("路径\t{_dir}\t{fs}".format(_dir=_dir, fs=fs))
        file.delete_file(_dir)
        fs = file.get_folder_size(_dir)
        print("路径\t{_dir}\t{fs}".format(_dir=_dir, fs=fs))
    after_disk_usage = shutil.disk_usage(".")
    print(before_disk_usage)
    print(after_disk_usage)


# Install click commands.
cli.add_command(unzip)
cli.add_command(rename)
cli.add_command(clean)
cli.add_command(summary)
cli.add_command(cleanmymac)

if '-' not in ''.join(sys.argv) and len(sys.argv) > 1:
    cli = DYMCommandCollection(sources=[cli])
if __name__ == '__main__':
    cli()
