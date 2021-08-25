string=input().upper()
time=0
for i in string:
    if i=='A' or i=='B'or i=='C':
        time+=2
    elif i=='D' or i=='E'or i=='F':
        time+=3
    elif i=='G' or i=='H'or i=='I':
        time+=4
    elif i=='J' or i=='K'or i=='L':
        time+=5
    elif i=='M' or i=='N'or i=='O':
        time+=6
    elif i=='P' or i=='Q'or i=='R'or i=='S':
        time+=7
    elif i=='T' or i=='U'or i=='V':
        time+=8
    elif i=='W' or i=='X'or i=='Y'or i=='Z':
        time+=9

print(time+len(string))



'다른풀이
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
ret = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            ret += dial.index(i)+3   // 1까지 가는데 1초 + index+2 ---> +3해줌
print(ret)
