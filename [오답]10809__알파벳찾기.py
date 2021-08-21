massage= input()
alphabet="abcdefghijklmnopqrstuvwxyz"

for i in alphabet:
    if i in massage:
        print(massage.index(i), end=' ')
    else:
        print(-1,end=' ')

