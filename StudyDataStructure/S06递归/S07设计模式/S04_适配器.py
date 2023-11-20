'''
模式：将一个类的接口转换成客户希望的另一个接口。适配器模式使得原本由于接口不兼容儿不能一起工作的类可以一起工作
实现方式：1、类适配器：使用多继承
2、对象适配器：使用组合
角色：
优点:1、
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

class BankPay:
    def cost(self, money):
        print("银联支付%d元" % money)

class ApplePay:
    def cost(self, money):
        print("苹果支付%d元" % money)

# # 适配器
# class NewBankPay(PayMent, BankPay):
#     def pay(self, money):
#         self.cost(money)

# 对象适配器
class PaymentAdapter(PayMent):
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)

p = PaymentAdapter(ApplePay())
p.pay(100)
