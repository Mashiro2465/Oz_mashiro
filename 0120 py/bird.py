def 앵무새 () :
    return """
        앵무새 출발!!!
        까악
        날게를 힘차게 날았습니다.
        결과는 2 m 입니다.
        """

def 참새 () :
    return """
        참새 출발!!!
        짹짹
        날게를 빠르게 날았습니다.
        결과는 8 m 입니다.
        """

def 비둘기 () :
    return """
        비둘기 출발!!!
        구구
        날게를 부드럽게 날았습니다.
        결과는 12 m 입니다.
        """

def 닭 () :
    return """
        닭 출발!!!
        꼬끼오
        날게를 퍼덕이며 날았습니다.
        결과는 6 m 입니다.
        """

def 러버덕 () :    
    return """
        러버덕 출발!!!
        삑삑삑
        날지 못했습니다...
        """


    
while(True) :
    bird = input("새이름은?? : ") 

    if(bird =="종료") : break

    try :
        if(bird =="앵무새") :
            print(앵무새())
        elif(bird =="참새") :
            print(참새())
        elif(bird =="비둘기") :
            print(비둘기())
        elif(bird =="닭") :
            print(닭())
        elif(bird =="러버덕") :
            print(러버덕())
        else : print("잘못된 입력입니다.")

    except :
        print("잘못된 입력입니다.")