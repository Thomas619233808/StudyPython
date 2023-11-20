'''
建造者模式：将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以有不同的表示
角色：
1、抽象建造者（Builder 2、具体建造者（Concrete Builder 3、指挥者（Director 4、产品（Product

优点：1、隐藏了产品的内部结构和装配过程
2、可将构造代码和表示代码分开
3、可以对构造过程进行更精细的空值
'''
from abc import ABCMeta, abstractmethod
class Player:
    def __init__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg

    def __str__(self):
        return "%s, %s, %s, %s" % (self.face, self.body, self.arm, self.leg)

class PlayerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_arm(self):
        pass

    @abstractmethod
    def build_leg(self):
        pass

class GirlBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "face1"

    def build_body(self):
        self.player.body = "body1"

    def build_arm(self):
        self.player.arm = "arm1"

    def build_leg(self):
        self.player.leg = "leg1"

class Monster(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "monsterface"

    def build_body(self):
        self.player.body = "monsterbody1"

    def build_arm(self):
        self.player.arm = "monsterarm1"

    def build_leg(self):
        self.player.leg = "monsterleg1"

class PlayerDirector:
    def build_player(self, builder):
        builder.build_body()
        builder.build_face()
        builder.build_arm()
        builder.build_leg()
        return builder.player

builer = GirlBuilder()
director = PlayerDirector()
p = director.build_player(builer)
print(p)