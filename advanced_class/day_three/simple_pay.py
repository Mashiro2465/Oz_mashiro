from abc import ABC, abstractmethod

#Product
class Pay(ABC):
    @abstractmethod
    def pay(self, amount: int) -> None:
        pass

#Concrete Products
class Kakao_pay(Pay):
    def pay(self, amount: int) -> None:
        print(f"💳 카카오페이로 {amount}원 결제")


class Naver_pay(Pay):
    def pay(self, amount: int) -> None:
        print(f"💳 네이버페이로 {amount}원 결제")

class GS_pay(Pay):
    def pay(self, amount: int) -> None:
        print(f"💳 GS페이로 {amount}원 결제")

#Factory
class Pay_factory:
    @staticmethod
    def create(method: str) -> Pay:
        if method == "kakao":
            return Kakao_pay()
        if method == "naver":
            return Naver_pay()
        if method == "gs":
            return GS_pay()
        raise ValueError("지원하지 않는 결제 수단")

payment = Pay_factory.create("kakao")
payment.pay(10000)
