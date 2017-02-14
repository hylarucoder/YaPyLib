import re

import sys

from yapylib.utils.str_util import PT_UUID, REGEXES


def has_pattern(_str, pattern):
    return bool(re.search(pattern, _str))


def match_pattern(_str, pattern):
    return bool(re.match(pattern, _str))


def find_first_matched_pattern(_str, pattern):
    arr = re.findall(pattern, _str)

    if len(arr) > 0:
        return arr[0]
    else:
        return None


def find_all_matched_pattern(_str, pattern):
    arr = re.findall(pattern, _str)
    if len(arr):
        return re.findall(pattern, _str)
    else:
        return None


for regex, regex_pattern in REGEXES.items():
    def has_regex_func(_str, regex_pattern=regex_pattern):
        return has_pattern(_str, regex_pattern)


    def is_regex_func(_str, regex_pattern=regex_pattern):
        return match_pattern(_str, regex_pattern)


    def extract_first_regex_func(_str, regex_pattern=regex_pattern):
        return find_first_matched_pattern(_str, regex_pattern)


    def extract_all_regex_func(_str, regex_pattern=regex_pattern):
        return find_all_matched_pattern(_str, regex_pattern)


    setattr(sys.modules[__name__], 'has_{regex_suffix}'.format(regex_suffix=regex), has_regex_func)
    setattr(sys.modules[__name__], 'is_{regex_suffix}'.format(regex_suffix=regex), is_regex_func)
    setattr(sys.modules[__name__], 'extract_first_{regex_suffix}'.format(regex_suffix=regex), extract_first_regex_func)
    setattr(sys.modules[__name__], 'extract_all_{regex_suffix}'.format(regex_suffix=regex), extract_all_regex_func)
