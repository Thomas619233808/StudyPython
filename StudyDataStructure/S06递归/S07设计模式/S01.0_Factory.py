'''
简单工厂模式：不直接向客户端暴露对象创建的实现细节，而是通过一个工厂类来实现。
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

class PaymentFactory:
    def create_payment(self, method):
        if method == 'alipay':
            return Alipay()
        elif method == 'wechat':
            return WechatPay()
        else:
            raise TypeError("No such payment name %s" %method)

pf = PaymentFactory()
p = pf.create_payment('alipay')
p.pay(100)


