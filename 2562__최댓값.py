// 내 풀이
a=[]                         //'list선언
for i in range(9):
    a.append(int(input()))

for j in range(9):
    if (int(max(a))==int(a[j])):
        print(max(a))
        print(j+1)

        

//다른풀이
a=[]
for i in range(9):
    a.append(int(input()))

print(max(a))
print(a.index(max(a))+1)
