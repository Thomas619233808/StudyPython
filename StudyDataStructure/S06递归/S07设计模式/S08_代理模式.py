'''
代理模式：为其它对象提供一个代理，以空值对这个对象的访问
应用场景：1、远程代理 2、虚代理 3、保护代理
角色：1、抽象实体（Subject 2、实体（RealSubject 3、代理（Proxy
优点:1、远程代理：可以隐藏对象位于远程地址空间的事实
2、虚代理：可以进行优化，例如根据需求创建对象
3、保护代理：允许在访问一个对象时有一些附加的内务处理
'''

from abc import ABCMeta,abstractmethod
#
class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self):
        pass

class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        f = open(filename, 'r', encoding='utf-8')
        print('读取文件内容')
        self.content = f.read()
        f.close()

    def get_content(self):
        return self.content

    def set_content(self, content):
        f = open(self.filename, 'w', encoding='utf-8')
        f.write(content)
        f.close()

class VirtualProxy(Subject):
    def __init__(self, filename):
        self.filename = filename
        self.subj = None

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()

    def set_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.set_content()

class ProtectedProxy(Subject):
    def __init__(self, filename):
        self.subj = RealSubject(filename)

    def get_content(self):
        return self.subj.get_content()

    def set_content(self):
        raise PermissionError("无写入权限")



#subj = RealSubject("test.txt")
subj2 = VirtualProxy("test.txt")
print(subj2.get_content())




