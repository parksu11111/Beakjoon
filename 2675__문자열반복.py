T = int(input())
for i in range(T):
    R,S= list(map(str,input().split()))
    for j in range(len(S)):
        print(S[j]*int(R),end='')
    print()
    
    
