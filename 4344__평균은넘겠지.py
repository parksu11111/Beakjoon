C = int(input())

for i in range(C):
    score=list(map(int,input().split()))
    avg = sum(score[1:])/score[0]
    high=0
    
    for j in score[1:]:
        if j > avg:
           high += 1
    rate = "{:.3f}%".format(high/score[0]*100)
    print(rate)
