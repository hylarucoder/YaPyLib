import os
import sys
import click

from click_didyoumean import DYMCommandCollection
import click_completion
import crayons

from yapylib.cmd.core import format_help
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
    The Must-Have Utils For Every Pythonista Since 2016.
    """
    # ctx.verbose = verbose
    click.echo(format_help(ctx.get_help()))


@click.command(
    short_help="unzip gbk package",
    context_settings=dict(ignore_unknown_options=True, allow_extra_args=True),
)
def unzip():
    click.echo("is unzipping gbk")
    pass


@click.command(
    short_help="execute python and then enter ipython",
    context_settings=dict(ignore_unknown_options=True, allow_extra_args=True),
)
def ishell():
    click.echo("is executing")
    pass


@click.command(
    short_help="execute python and then enter ipython",
    context_settings=dict(ignore_unknown_options=True, allow_extra_args=True),
)
@click.argument('url', required=True, type=click.STRING)
def fetch_and_ishell():
    click.echo("is executing")
    pass


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
    pass


@click.command(
    short_help="self testing",
    context_settings=dict(ignore_unknown_options=True, allow_extra_args=True),
)
def summary():
    click.echo("is self test")
    pass


@click.command(
    short_help="what the file?",
    context_settings=dict(ignore_unknown_options=True, allow_extra_args=True),
)
def wtf():
    click.echo("is self test")
    pass


# Install click commands.
cli.add_command(unzip)

if '-' not in ''.join(sys.argv) and len(sys.argv) > 1:
    cli = DYMCommandCollection(sources=[cli])
if __name__ == '__main__':
    cli()
