N = int(input())
score = list(map(int, input().split()))
M = max(score)

new_score=[]
for i in score:
    new_score.append(i/M*100)
print(sum(new_score)/N)




'for문에 range대신 배열사용 -----> 인수(i)에 배열이 차례로 들어감
'파이썬엔 avg함수없음 ----> sum과 len 이용해서 평균구함
