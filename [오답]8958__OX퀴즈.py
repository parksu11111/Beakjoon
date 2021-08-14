n = int(input())

for i in range(n):
    a = str(input())
    a_list=list(a)
    score=0
    con=1
    for j in a:
       if  j=="O":
           score+=con
           con+=1
          
       else:
           con=1
       
    print(score)
    
