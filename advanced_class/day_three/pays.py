from pay import Pay

class Kakao_pay(Pay) :
    def pay(self, amount) :
        print(f"카카오 페이로 {amount}원 결제")


class naver_pay(Pay):
    def pay(self, amount):
        print(f"네이버 페이로 {amount}원 결제")


class gs_pay(Pay):
    def pay(self, amount):
        print(f"지에스 페이로 {amount}원 결제")
