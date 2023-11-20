'''
模式：定义一系列算法，把它们一个个封装起来，且使它们之间可以相互替换。
该模式可使算法独立于使用它的客户而变化
角色：1、抽象策略（Strategy  2、具体策略（ConcreteStrategy  3、上下午（Context
场景：1、
优点：1、定义了一系列可重复使用的算法和行为
2、消除了一些条件语句
3、可以提供相同行为的不同实现
缺点：1、客户必须了解不同的策略
'''
from abc import ABCMeta, abstractmethod

class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, data):
        pass

class FastStrategey(Strategy):
    def execute(self, data):
        print("Fast Strategy %s" % data)

class SlowStrategy(Strategy):
    def execute(self, data):
        print("Slow Strategy %s" % data)

class Context:
    def __init__(self, strategy, data):
        self.data = data
        self.strategy = strategy

    def set_strategy(self, strategy): # 更改策略
        self.strategy = strategy

    def do_strategy(self): # 执行策略
        self.strategy.execute(self.data)

data = "[...]"
s = FastStrategey()
context = Context(s, data)
context.do_strategy()
context.set_strategy(SlowStrategy())
context.do_strategy()

