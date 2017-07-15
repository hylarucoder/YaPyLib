import click
import pytest
from yapylib.cli import pass_context


@click.command('test', short_help='run tests with py.test')
@pass_context
def cli(ctx):
    """使用REQUESTS请求某个地址,跳转到IPython便于下一步解析."""
    ctx.log('正在测试')
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
    pytest.cmdline.main(args_str)
