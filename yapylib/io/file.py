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
