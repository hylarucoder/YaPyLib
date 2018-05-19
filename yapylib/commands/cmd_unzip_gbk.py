import click

from yapylib.cli import pass_context
from yapylib.utils.file_utils import unzip_gbk_file


@click.command('unzip_gbk', short_help='unzip_gbk')
@click.argument('path', required=True, type=click.STRING)
@pass_context
def cli(ctx, path):
    """
    example:

     - yapylib unzip_gbk compressed.zip uncompressed
    """
    unzip_gbk_file(path, None)
