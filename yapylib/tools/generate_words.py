"""
1. 从字幕中抽取所有单词,并且进行还原
2.
"""
import os
import re
from collections import Counter


def get_all_words(filename):
    """
    :param filename:
    :return:
    """
    print(filename)
    all_words = set()
    try:
        all_words = re.findall("[a-zA-Z]+", open(filename).read(), flags=re.ASCII)
    except Exception:
        all_words = re.findall("[a-zA-Z]+", open(filename, encoding='gbk').read(), flags=re.ASCII)
    finally:
        filtered_words = set()
        for word in all_words:
            if len(word) <= 2:
                continue
            word = word.lower()
            filtered_words.add(word)
        return filtered_words


def get_all_file():
    filename = "/Users/twocucao/Downloads/PersonOfInterested/"
    all_folders = [os.path.join(filename, folder) for folder in os.listdir(filename)]
    print(all_folders)
    all_files = []
    for folder in all_folders:
        all_files.extend([os.path.join(folder, file) for file in os.listdir(folder)])

    all_words = set()
    for file in all_files:
        words = get_all_words(file)
        all_words.update(words)

    a = list(all_words)
    a.sort()
    with open("all_words.txt", "wt") as f:
        for i in a:
            f.write(i)
            f.write("\n")
