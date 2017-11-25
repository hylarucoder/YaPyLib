# https://stackoverflow.com/questions/31875/is-there-a-simple-elegant-way-to-define-singletons

def singleton(cls):
    """
    :param cls:
    :return:

    单例的装饰器实现
    """

    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return get_instance


"""
@singleton
class MyClass:
    pass
    
# TODO: 有机会补充测试
"""
