from abc import ABC, abstractmethod

# 커피 자판기, 콜라 자판기, 라면 자판기를 템플릿 메서드 패턴으로 설계해 보세요.
#
# 모든 자판기는 아래와 같은 공통 흐름으로 음료/식품을 제공합니다.
#
# 돈 투입 - 고객이 금액을 넣는다.
# 금액 검증 - 투입 금액이 제품 가격 이상인지 확인한다.
# 제품 준비 - 자판기 종류에 따라 다른 방식으로 제품을 준비한다. (구체 자판기마다 다름)
# 제품 배출 - 준비된 제품을 내보낸다.
# 거스름돈 반환 - 잔액이 있으면 반환한다.

class vending_machine (ABC) :
    def __init__(self, name : str, price : int) :
        self.name = name
        self.price = price

    #템플릿 메서드
    def serve(self, amount : int) :
        self.insert_money(amount)
        self.product_price(amount)
        self.selected_product()
        self.dispensed_product()
        self.change_amount(amount)


    # 돈 투입 - 고객이 금액을 넣는다.
    def insert_money(self,amount :int) :
        print(f"[{self.name}] 돈 투입: {amount}원")

    # 금액 검증 - 투입 금액이 제품 가격 이상인지 확인한다.
    def product_price(self, amount :int) :
        if amount < self.price:
            raise ValueError(f"[{self.name}] 금액 부족 (필요: {self.price}원)")
        print(f"[{self.name}] 금액 검증 완료 (필요: {self.price}원)")

    # 제품 준비 - 자판기 종류에 따라 다른 방식으로 제품을 준비한다. (구체 자판기마다 다름)
    @abstractmethod
    def selected_product(self) :
        pass

    # 제품 배출 - 준비된 제품을 내보낸다.
    def dispensed_product(self) :
        print(f"[{self.name}] 제품 배출 완료")

    # 거스름돈 반환 - 잔액이 있으면 반환한다.
    def change_amount(self, amount) :
        change =amount - self.price
        if change > 0 :
            print(f"[{self.name}] 거스름돈 {change}원 반환")
        else :
            print(f"[{self.name}] 거스름돈 없음")