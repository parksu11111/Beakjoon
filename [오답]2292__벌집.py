# Q. 문제 == 주어진 숫자의 벌집의 겹수를 구해라

N = int(input())


cnt=1    #-벌집의 겹수
nums=1   #-번호


if N==1:
    print(1)
    
else:
    while(N > nums):
        nums = nums + 6*cnt   #- 벌집의 겹이 6의 배수로 증가 (1,6,12,18 ...) 
        cnt +=1 
    print(cnt)
    
    
    
    
    # 1겹 : 1
    # 2겹 : 2~7 (1겹+6*1)
    # 3겹 : 8~19 (2겹+6*2)
    # 4겹 : 20 ~ 37 (3겹+6*3)
    ...
