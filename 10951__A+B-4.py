while True:
    try:
        A,B = map(int, input().split())
        print(A+B)

    except:
        break
        
       'try except문 안하면 런타임 에러
       'except:예외처리
