//나의 풀이
H,M= map(int,input().split())

if H-1 < 0 and M <45:
    print(23,M+15)

elif H-1 < 0 and M>=45 :
    print(H,M-45)

elif H>0 and  M<45 :
    print(H-1,M+15)
    
elif H>0 and M>=45:
    print(H,M-45)
    
    
    
//다른 풀이
H,M= map(int,input().split())

M= M-45     //M에서 45분 뺌

if M<0 :  
    H-=1   //시간에서 꿔온다
    M+=60  //분에 60분 더해준다

if H<0:   //H-1이 음수라면( H가 0일경우)
    H+=24  // 24시 더해줌 (-1시 ---> 23시)

print(H,M)

