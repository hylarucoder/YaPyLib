import crayons


def format_help(help):
    help = help.replace('Options:', str(crayons.white('Options:', bold=True)))
    help = help.replace(
        'Usage: yapylib',
        str('Usage: {0}'.format(crayons.white('yapylib', bold=True))),
    )

    help = help.replace('  unzip', str(crayons.red('  unzip', bold=True)))

    additional_help = """
    Usage Examples:
       unzip a zip file with gbk encoding
       $ {1}
       hahah
       $ {2}
    Commands:""".format(
        crayons.red('yapylib --three'),
        crayons.red('yapylib install --dev'),
        crayons.red('yapylib run pip freeze'),
    )
    help = help.replace('Commands:', additional_help)
    return help
