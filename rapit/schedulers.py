

class BaseScheduler(object):
    """
    调度器基类
    """
    pass


class SequentialScheduler(BaseScheduler):
    pass


class ConcurrentScheduler(BaseScheduler):
    """
    并行任务调度器
    """
    pass


class DependenciesScheduler(BaseScheduler):
    """
    依赖关系调度器
    """
    pass


