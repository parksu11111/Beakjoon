'틀림

n = num = int(input())
N = 0                 '//횟수

while True:
    ten = n // 10
    one = n % 10
    total = ten + one
    
    N += 1
    
    n = int(str(n % 10) + str(total % 10))
    
    if(num == n):
        break
print(N)
