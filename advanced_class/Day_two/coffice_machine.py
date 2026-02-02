from vending_machine import vending_machine

class coffice_machine(vending_machine) :
    def __init__(self):
        super().__init__("커피 자판기", 1200)

    def selected_product(self) :
        print("[커피 자판기] 원두 분쇄 중...")
        print("[커피 자판기] 추출 중...")
        print("[커피 자판기] 컵에 담는 중...")