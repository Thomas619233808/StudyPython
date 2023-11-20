'''
模式：定义一个操作中的算法的骨架，而将一些步骤延迟到子类中。使得子类在不改变算法结构的情况下也能重定义某些算法步骤
角色：1、抽象类（AbstractClass  2、具体类（ConcreteClass
场景：1、一次性实现一个算法的不变的部分
2、各个子类的公共行为应该被提取出来并集中到一个公共父类中以避免代码重复
3、控制子类拓展
优点：1、
'''
from abc import ABCMeta, abstractmethod
from  time import sleep

class Window(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def repaint(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def run(self): # 模板方法
        self.start()
        while True:
            try:
                self.repaint()
                sleep(1)
            except KeyboardInterrupt:
                break
        self.stop()

class Mywindow(Window):
    def __init__(self, msg):
        self.msg = msg

    def start(self):
        print("start")

    def stop(self):
        print("stop")

    def repaint(self):
        print(self.msg)

Mywindow("Hello").run()
