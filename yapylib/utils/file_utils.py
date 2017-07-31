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


"""
下面的程序主要用于MacOS上一些程序的调用
"""


def open_image():
    pass


def open_url():
    pass


def open_video():
    pass
