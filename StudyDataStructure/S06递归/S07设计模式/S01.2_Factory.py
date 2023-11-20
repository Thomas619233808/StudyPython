'''
工厂方法模式：
优点：1、每个具体产品对应一个具体工厂类，不需要修改工厂类代码
2、隐藏了对象创建的实现细节
缺点：1、没增加一个具体产品类，就必须增加一个相应的具体工厂类
'''

from abc import ABCMeta, abstractmethod
class PayMent(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass

class Alipay(PayMent):
    def pay(self, money):
        print("支付宝支付%d元。" %money)

class WechatPay(PayMent):
    def pay(self, money):
        print("微信支付%d元。" % money)

class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass

class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()

class WechatPayFactory(PaymentFactory):
    def create_payment(self):
        return WechatPay

pf = AlipayFactory()
p = pf.create_payment()
p.pay(100)



