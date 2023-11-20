'''
模式：定义对象间的一种一对多的依赖关系，当一个对象的状态发生改变，它所依赖的对象都得到通知并更新
观察者模式又称为 “发布-订阅”模式
角色：1、抽象主题（Subject  2、具体主题（ConcreteSubject  3、抽象观察者（Observer  4、具体观察者（ConcreteObserver
场景：1、当一个抽象模型有两方面，其中一个方面依赖于另一方面。将两者单独封装的独立对象，使它们可以单独改变、复用
2、当对一个对象的改变需要同事改变其它对象，而不知道具体有哪些对象待改变
3、当一个对象必须通知其它对象，而它又不能假定其它对象是谁，换言之，不希望对象紧密耦合
优点：1、目标和观察者之间的抽象耦合最小
2、支持广播通信
'''
from abc import ABCMeta, abstractmethod

class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, notice):
        pass

class Notice:
    def __init__(self):
        self.observers = [] # 订阅者列表

    def attach(self, obs): # 添加订阅者
        self.observers.append(obs)

    def detach(self, obs): # 删除订阅者
        self.observers.remove(obs)

    def notify(self): # 推送消息给订阅者
        for obs in self.observers:
            obs.update(self)

class StaffNotice(Notice): # 具体发布者
    def __init__(self, company_info):
        super().__init__()
        self.__company_info = company_info

    @property
    def company_info(self):
        return self.__company_info

    @company_info.setter
    def company_info(self, info):
        self.__company_info = info
        self.notify() # 推送

class Staff(Observer): # 具体订阅者
    def __init__(self):
        self.company_info = None

    def update(self, notice):
        self.company_info = notice.company_info

notice = StaffNotice("start")
s1 = Staff()
s2 = Staff()
notice.attach(s1)
notice.attach(s2)
notice.company_info = "123"
print(s1.company_info)
print(s2.company_info)
notice.detach(s2)
notice.company_info = "456"
print(s1.company_info)
print(s2.company_info)
