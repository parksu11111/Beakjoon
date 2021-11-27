[실패한 코드 1 ]  -> 시간초과됨 
#작은 숫자는 실행가능하지만 큰 수 넣을 시 시간초과됨

A,B,C = input().split()
A= int(A)
B= int(B)
C= int(C)

i=1

while (1):
    if (A/(C-B) < 0):
        print (-1)
        break;
    
    if (i > int(A/(C-B))):
        print(i)
        break;
    
    else:
        i=i+1
        continue

 [실패한코드 2] -> 얘도 시간초과
import sys
A,B,C = list(map(int,sys.stdin.readline().split()))  //#- 여러문자를 입력받을 시 input() 보다 sys.stdin.readline() 이용하는게 빠름 --> 맨 위에 import sys 추가

i=1

while (1):
    if (A/(C-B) < 0):
        print (-1)
        break;
    
    if (i > int(A/(C-B))):
        print(i)
        break;
    
    else:
        i=i+1
        continue
        
        
        
 [성공코드]
import sys
A,B,C = list(map(int,sys.stdin.readline().split()))   //#- A,B,C = list(map(int, input().split())) 과 같음

if B>=C :
    print(-1)

else:
    print(int(A/(C-B))+1)
   
