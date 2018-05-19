import os


def get_load_dotenv(default=True):
    val = os.environ.get('YAPYLIB_SKIP_DOTENV')
    if not val:
        return default
    return val.lower() in ('0', 'false', 'no')
