# coding=utf-8
import time
from yapylib.profile.pprogress import GeneratorProgressBar


def process(a):
    time.sleep(1)
    return a


def test_GeneratorProgressBar():
    def process_tasks_gene(tasks):
        for task in tasks:
            task_result = process(task)
            yield task_result

    tasks = [1, 2, 3]
    gene = process_tasks_gene(tasks)
    GeneratorProgressBar(0, len(tasks), 1, gene).begin()
    gene = process_tasks_gene(tasks)
    GeneratorProgressBar(0, None, 1, gene).begin()
