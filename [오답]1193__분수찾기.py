

x=int(input())

line =0           #- 몇 번째 라인
num_index=0       #- 숫자 인덱스

while x > num_index:   #- 입력받은숫자가 숫자인덱스보다 클 때 반복해라
    line += 1          #- 라인은 1씩 늘어감
    num_index += line  #- 인덱스는 1,1+2,1+2+3 ... 이런식으로 개수가 늘어감

gap = num_index-x      #- 숫자인덱스 - 입력받은 숫자

if line % 2 == 0:      #-짝수번째 라인이면
    top = line-gap     #-분자
    bottom = gap + 1   #-분모는 1씩 늘어감
    
else:                  #-홀수번째 라인이면
    top = gap + 1      #-분자는 1씩 늘어감
    bottom = line - gap  #-분모

print("%d/%d"%(top,bottom)) #- "0/0" 형태로 출력

