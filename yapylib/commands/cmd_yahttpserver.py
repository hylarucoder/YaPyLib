import click

from yapylib.cli import pass_context
from yapylib.tools.yahttpserver import serve_yahttpserver


@click.command('yahttpserver', short_help='yet another http.server with flask && react')
@pass_context
def cli(ctx):
    """使用REQUESTS请求某个地址,跳转到IPython便于下一步解析."""
    ctx.log('正在开启')
    serve_yahttpserver()
