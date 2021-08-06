N = input()

for i in range(1,int(N)+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
    
    
    
 '다른풀이
inp = int(input())     
for i in range(1,(inp+1)):
    print("*" * i)   //  *을 i 만큼 반복출력 
