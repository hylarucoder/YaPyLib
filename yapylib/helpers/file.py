import os

import shutil

"""
1. 格式化文件大小
2. 根据路径删除文件 / force 删除文件树
3. 返回文件扩展名称
4. 读取文本内容并返回
"""


def format_size(num_str, digit_num=2):
    pass


def abs_path(path):
    if path.startwith("~"):
        return os.path.expanduser(path)
    else:
        return os.path.abspath(path)
    pass


def delete_file(path):
    os.remove(path)
    return not file_exist(path)


def parent_folder(path):
    return os.path.dirname(path)


def list_subfolder_files(path):
    return [val for sublist in [[os.path.join(i[0], j) for j in i[2]] for i in os.walk(path)] for val in sublist]


def delete_folder_content(dir_path):
    """
    :param dir_path:
    :param force:
    :return:
    删除文件夹中的错有内容
    """
    file_list = os.listdir(dir_path)
    for file in file_list:
        path = dir_path + "/" + file
        shutil.rmtree(path)
        return not file_exist(path)


def delete_folder(path, force=False):
    if force:
        shutil.rmtree(path)
    else:
        os.rmdir(path)
    return not file_exist(path)


def read_file(path):
    return open(path).read()


def file_exist(path):
    return os.path.exists(path)


def write_file(path, content):
    open(path, 'wt').write(content)


def get_folder_size(start_path='.', recursive=True):
    if recursive:
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size
    else:
        return sum(os.path.getsize(f) for f in os.listdir('.') if os.path.isfile(f))


def copy_file(src, dst):
    shutil.copy(src, dst)


def copy_folder(src, dst):
    shutil.copytree(src, dst)


def rename_file(src, dst):
    shutil.move(src, dst)


def unzip_file():
    pass


def unzip_gbk_file(origin, target=None):
    """
    author: YUCOAT(yucoat^http://yucoat.com)
    modified by: twocucao

    用于解压windows传到mac文件上面的编码问题
    """
    import os
    import zipfile
    import click
    if not target:
        target = "./{}".format(origin.split(".zip")[0])
    if not os.path.exists(target):
        os.makedirs(target)

    zip_obj = zipfile.ZipFile(origin, 'r')
    for name in zip_obj.namelist():
        target_file_name = "{}/{}".format(target, name.encode('cp437').decode('gb18030'))
        target_file_folder = os.path.dirname(target_file_name)
        if (not os.path.exists(target_file_folder)) and target_file_folder:
            os.makedirs(target_file_folder)
        content = zip_obj.read(name)
        if not os.path.exists(target_file_name):
            tmp = open(target_file_name, 'wb')
            tmp.write(content)
            tmp.close()
        print('Exacting %s ... done!' % (target_file_name))
    zip_obj.close()


from enum import Enum


class FILESIZE(Enum):
    L_FILE = 1
    XL_FILE = 2
    XLL_FILE = 3


class FileReader(object):
    """
    用于数据分析时候对文件做预判
    """

    def __init__(self, path, mode, compression=None):
        """
        :param path:
        :param mode:
        :param compression:
        """
        # GZ Compression
        if compression == 'gzip':
            import gzip
            f = gzip.open(path, mode)
        # BZ Compression
        elif compression == 'bz2':
            import bz2
            f = bz2.BZ2File(path, mode)
        else:
            f = open(path, mode, encoding="utf-8")

        self.f = f

    def info(self):
        pass

    def head(self, start, end):
        pass

    def tail(self, start, end):
        pass

    def cat(self, start, end):
        pass

    def info(self):
        sum(1 for line in open('myfile.txt'))
        pass

    def read_items(self, sep="\n", compression=None):
        pass


class FileWriter(object):
    def __init__(self):
        pass

    def append(self):
        pass

    def read_items(self, sep="\n", compression=None):
        pass


class File(object):
    pass


class FileTrans(object):
    pass


def getlineno(path, mode, compression=None):
    """
    :param path:
    :param mode:
    :param compression:
    :return:
    fast count file number
    """
    # GZ Compression
    if compression == 'gzip':
        import gzip
        f = gzip.open(path, mode)
    # BZ Compression
    elif compression == 'bz2':
        import bz2
        f = bz2.BZ2File(path, mode)
    else:
        f = open(path, mode, encoding="utf-8")

    return sum(1 for line in f)
