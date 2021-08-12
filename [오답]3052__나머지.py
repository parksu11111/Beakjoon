a=[]
c=[]
cnt=int(1)

for i in range(10):
    a.append(int(input()))
    c.append(int(a[i]%int(42)))
print(len(set(c)))       






//'set(리스트명) -----> 중복값제거 
