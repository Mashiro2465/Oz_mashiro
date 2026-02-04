from coffice_machine import coffice_machine
from coke_machine import coke_machine
from noodle_machine import noodle_machine

def main():
    machines = {
        "1": coffice_machine(),
        "2": coke_machine(),
        "3": noodle_machine()
    }

    print("====== 자판기 선택 ======")
    print("1. 커피 자판기 (1200원)")
    print("2. 콜라 자판기 (800원)")
    print("3. 라면 자판기 (1500원)")
    print("=========================")

    choice = input("자판기를 선택하세요 (1~3): ")

    if choice not in machines:
        print("잘못된 선택입니다.")
        return

    amount = int(input("투입할 금액을 입력하세요: "))
    machines[choice].serve(amount)

if __name__ == "__main__":
    main()

