import json

import click
import parsel
from yapylib.cli import pass_context
from yapylib.utils.type_util import is_html, is_json
from yapylib.wrapped.requests import session


@click.command('fetch', short_help='fetch a url and parse response.')
@click.argument('url', required=True, type=click.STRING)
@pass_context
def cli(ctx, url):
    """使用REQUESTS请求某个地址,跳转到IPython便于下一步解析."""
    ctx.log('正在请求网址 %s', url)
    from IPython import embed

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
