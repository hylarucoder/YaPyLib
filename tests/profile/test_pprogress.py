# coding=utf-8
import time

from yapylib.profile.pprogress import GeneratorProgressBar
from yapylib.profile.ptime import timethis
from yapylib.logging import get_logger


def process(a):
    import time
    time.sleep(1)
    return a


def test_GeneratorProgressBar():
    def process_tasks_gene(tasks):
        for task in tasks:
            v = process(task)
            yield v

    tasks = [1, 2, 3]
    gene = process_tasks_gene(tasks)
    GeneratorProgressBar(0, len(tasks), 1, gene).begin()
    gene = process_tasks_gene(tasks)
    GeneratorProgressBar(0, None, 1, gene).begin()
