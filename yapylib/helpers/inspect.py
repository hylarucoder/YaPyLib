import inspect
import string

from yapylib.helpers.type_utils import is_str

for name, value in inspect.getmembers(string, is_str):
    if name.startswith('_'):
        continue
    print('%s=%r\n' % (name, value))
