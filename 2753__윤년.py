year = int(input())

if (year%4 ==0 and year % 100 != 0) or (year % 400 == 0):    // 윤년: 4의 배수이면서 100의 배수는 아니거나 400의 배수인 년도
    print('1')
else:
    print('0')
