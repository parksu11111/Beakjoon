A=int(input())
B=int(input())
C=int(input())
D=list(str(A*B*C))             //'str로 list형태로 저장시킴

for i in range(10):         
    print(D.count(str(i)))           //'개수세기------> ~.count()
