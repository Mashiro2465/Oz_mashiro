class Birds () :
    def __init__(self, name, sound, fly, distince):
        self.name = name
        self.sound = sound
        self.fly = fly
        self.distince = distince

    def __str__(self):
        return f"""
            {self.name} 출발!!!
            {self.sound}
            날게를 {self.fly} 날았습니다.
            결과는 {self.distince} m 입니다.
        """
    
brids = {
    "앵무새" : Birds("앵무새", "까악", "힘차게", 2),
    "참새" : Birds("참새", "짹짹", "빠르게게", 8),
    "비둘기" : Birds("비둘기", "구구", "부드게", 12),
    "닭" : Birds("닭", "꼬끼오", "퍼덕이며", 6),
    "러버덕" : Birds("러버덕", "삑삑삑", "펴지못해 못", 0),
}


while(True) :
    bird = input("새이름은?? : ") 

    if(bird =="종료") : break

    try :
        print(birds[bird])
    except :
        print("잘못된 입력입니다.")
