import click
from yapylib.cli import pass_context
from yapylib.utils.nlp_utils.dnw_utils import dnw_4_bilibili


@click.command('fnw', short_help='find new words')
@click.argument('file_path', required=False, type=click.Path(resolve_path=True))
@pass_context
def cli(ctx, file_path):
    """使用REQUESTS请求某个地址,跳转到IPython便于下一步解析."""
    ctx.log('正在对文件 %s 进行分析'.format(file_path))
    dnw_4_bilibili(open(file_path).read()).to_excel("新词发现结果.xlsx")
