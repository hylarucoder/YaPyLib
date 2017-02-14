import inspect
import string

from yapylib.utils.type_util import is_str

for name, value in inspect.getmembers(string, is_str):
    if name.startswith('_'):
        continue
    print('%s=%r\n' % (name, value))
