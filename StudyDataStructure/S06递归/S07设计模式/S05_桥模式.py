'''
模式：将一个事物的两个维度分离，使其都可以独立地变化
2、角色：1、抽象  2、细化抽象  3、实现者  4、具体实现者
优点:1、抽象和实现分离
2、优秀的扩展能力
'''

from abc import ABCMeta, abstractmethod
class Shape(metaclass=ABCMeta):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass

class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self, shape):
        pass

class Rectangle(Shape):
    name = "长方形"
    def draw(self): # 长方形
        self.color.paint(self)

class Circle(Shape):
    name = '圆形'
    def draw(self):
        self.color.paint(self)

class Red(Color):
    def paint(self, shape):
        print('红色的%s' % shape.name)

class Green(Color):
    def paint(self, shape):
        print('绿色的%s' % shape.name)


shape = Rectangle(Red())
shape.draw()


