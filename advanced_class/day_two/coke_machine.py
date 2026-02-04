from vending_machine import vending_machine

class coke_machine(vending_machine) :
    def __init__(self):
        super().__init__("콜라 자판기", 800)

    def selected_product(self) :
        print("[콜라 자판기] 냉장 상태 확인 중...")
        print("[콜라 자판기] 배출구로 이동 중...")