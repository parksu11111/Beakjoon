import sys        'sys 정의 (sys.stdin.readline()을 사용하기 위헤)
T = int(sys.stdin.readline())  'input() 대신 sys.stdin.readline() 을 사용할 수 있다. 하지만 이때는 \n과 같은게 따라온다. 그래서 int 로 변환하여 없앤다. 또는 뒤에 .rstrip()룰 추가한다.

for i in range(T):
    a,b=  map (int,sys.stdin.readline().split())
    print(a+b)
