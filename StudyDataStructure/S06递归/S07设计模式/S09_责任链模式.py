'''
责任链模式：使多个对象都有机会处理请求，从而避免请求的发送者饿接收者之间的耦合关系。
将这些对象连成一条链，并沿着这条链传递该请求，直到有一个对象处理它为止
角色：1、抽象处理者  2、具体处理者  3、客户端
场景：1、有多个对象可以处理一个请求，哪个对象处理由运行时决定
2、在不明确接收者的情况下，向多个对象中的一个 提交一个请求
优点：1、降低耦合度
'''
from abc import ABCMeta, abstractmethod

class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handle_leave(self):
        pass

class GeneralManager(Handler):
    def handle_leave(self, day):
        if day <= 10:
            print("总经理准假%d天" % day)
        else:
            print("你还是辞职吧")

class DepartmentManager(Handler):
    def __init__(self):
        self.next = GeneralManager()

    def handle_leave(self, day):
        if day <= 5:
            print("部门经理准假%d天" % day)
        else:
            print("部门经理权限不足")
            self.next.handle_leave(day)

class ProjectDirector(Handler):
    def __init__(self):
        self.next = DepartmentManager()

    def handle_leave(self, day):
        if day <= 3:
            print("项目主管准假%d天" % day)
        else:
            print("项目主管权限不足")
            self.next.handle_leave(day)



day = 10
h = ProjectDirector()
h.handle_leave(day)