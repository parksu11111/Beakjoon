def han_num():
    num=0

    n= input()

    for i in range(1,int(n)+1):
        if i<100:
            num+=1
        else:
            if (i//100)-((i%100)//10) is ((i%100)//10) - i%10:
                num+=1
    print(num)
                                       
            
han_num()
   
