from vending_machine import vending_machine

class noodle_machine(vending_machine) :
    def __init__(self):
        super().__init__("라면 자판기", 1500)

    def selected_product(self) :
        print("[라면 자판기] 컵면 배출")
        print("[라면 자판기] 뜨거운 물 주입 중...")