'''
模式：给子系统中的一组接口提供一个一致的界面，外观模式定义了一个高层接口，使得子系统更易用
2、角色：1、外观 2、子系统类
优点:1、减少系统相互依赖 2、提高灵活性 3、提高安全性
'''

#
class CPU:
    def run(self):
        print("CPU开始运行")

    def stop(self):
        print("CPU停止运行")

#
class Disk:
    def run(self):
        print("硬盘开始工作")

    def stop(self):
        print("硬盘停止运行")

#
class Memory:
    def run(self):
        print("内存通电")

    def stop(self):
        print("内存断电")

class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.disk = Disk()
        self.memory = Memory()

    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()

computer = Computer()
computer.run()
computer.stop()



