num1,num2=list(map(str,input().split()))

if int(num1[::-1]) > int(num2[::-1]):
    print(int(num1[::-1]))

elif int(num1[::-1]) < int(num2[::-1]):
    print(int(num2[::-1]))

    
