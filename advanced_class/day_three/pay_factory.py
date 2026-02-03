from abc import ABC, abstractmethod

class Pay_factory(ABC) :
    @staticmethod
    def pay_doing(self, amount) :
        pay = self.pay(amount)
