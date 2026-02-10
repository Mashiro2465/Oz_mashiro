from abc import ABC, abstractmethod

#Product
class Store(ABC):
    @abstractmethod
    def pay(self, amount: int) -> None:
        pass

#Concrete Products
class Kakao_pay(Store):
    def pay(self, amount: int) -> None:
        print(f"💳 카카오페이로 {amount}원 결제")

class Naver_pay(Store):
    def pay(self, amount: int) -> None:
        print(f"💳 네이버페이로 {amount}원 결제")

class GS_pay(Store):
    def pay(self, amount: int) -> None:
        print(f"💳 GS페이로 {amount}원 결제")


#Creator
class Pay(ABC):
    def process(self, amount: int) -> None:
        payment = self.create_pay()
        payment.pay(amount)

    @abstractmethod
    def create_pay(self) -> Pay: #팩토리 메소드
        pass


#Concrete Creators
class Kakao_pay_use(Pay):
    def create_pay(self) -> Store:
        return Kakao_pay()


class Naver_pay_use(Pay):
    def create_pay(self) -> Store:
        return Naver_pay()


class GS_pay_use(Pay):
    def create_pay(self) -> Store:
        return GS_pay()


service = Kakao_pay_use()
service.process(10000)

service = Naver_pay_use()
service.process(20000)