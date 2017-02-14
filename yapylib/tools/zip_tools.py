"""
author: YUCOAT(yucoat^http://yucoat.com)
modified by: twocucao

1. 用于解压windows传到mac文件上面的编码问题
"""

import os
import sys
import zipfile


def gbk_zip(origin, target=None):
    zip_obj = zipfile.ZipFile(origin, 'r')
    for name in zip_obj.namelist():
        name_utf8 = name.decode('gb2312')
        path = os.path.dirname(name_utf8)
        if (not os.path.exists(path)) and path:
            os.makedirs(path)
        filedata = zip_obj.read(name)
        if not os.path.exists(name_utf8):
            tmp = open(name_utf8, 'w')
            tmp.write(filedata)
            tmp.close()
        print('Exacting %s ... done!' % (name_utf8))
    zip_obj.close()
