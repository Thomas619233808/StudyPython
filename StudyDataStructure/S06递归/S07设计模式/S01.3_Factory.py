'''
抽象工厂模式：定义一个工厂类接口，让工厂子类来创建一系列相关或相互依赖的对象
角色：1、抽象工厂 2、具体工厂 3、抽象产品 4、具体产品 5、客户端
优点：1、将客户端与类的具体实现相分离
2、每个工厂创建了一个完整的产品系列，使得易于交换系列
3、有利于产品的一致性
缺点：1、难以支持新种类的加入
'''
from abc import ABCMeta, abstractmethod

# 抽象产品
class PhoneShell(metaclass=ABCMeta):
    @abstractmethod
    def show_shell(self):
        pass

class CPU(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass

class OS(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        pass

# 抽象工厂
class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_shell(self):
        pass

    @abstractmethod
    def make_cpu(self):
        pass

    @abstractmethod
    def make_os(self):
        pass

# 具体产品
class SmallShell(PhoneShell):
    def show_shell(self):
        print("普通手机小手机壳")

class BigShell(PhoneShell):
    def show_shell(self):
        print("普通手机大手机壳")

class AppleShell(PhoneShell):
    def show_shell(self):
        print("苹果手机壳")

class SnapDragonCPU(CPU):
    def show_cpu(self):
        print("骁龙CPU")

class MediaTekCPU(CPU):
    def show_cpu(self):
        print("发哥CPU")

class AppleCPU(CPU):
    def show_cpu(self):
        print("发哥CPU")

class AppleOS(OS):
    def show_os(self):
        print("IOS")

class AndroidOS(OS):
    def show_os(self):
        print("Android")

# 具体工厂
class MiFactory(PhoneFactory):
    def make_cpu(self):
        return SnapDragonCPU()

    def make_os(self):
        return AndroidOS()

    def make_shell(self):
        return BigShell()

class AppleFactory(PhoneFactory):
    def make_cpu(self):
        return AppleCPU

    def make_os(self):
        return AppleOS

    def make_shell(self):
        return AppleShell

# 客户端
class Phone:
    def __init__(self, cpu, os, shell):
        self.cpu = cpu
        self.os = os
        self.shell = shell

    def show_info(self):
        print("手机信息：")
        self.cpu.show_cpu()
        self.os.show_os()
        self.shell.show_shell()

def make_phone(factory):
    cpu = factory.make_cpu()
    os = factory.make_os()
    shell = factory.make_shell()
    return Phone(cpu, os, shell)

p1 = make_phone((MiFactory()))
p1.show_info()
