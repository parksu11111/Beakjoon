word= input().upper()        #대문자로   hello --> HELLO
word2= list(set(word))       #중복제거하고 리스트로만듦  HEL0

cnt_list = []   

for i in word2:            # i = H,E,L,O
    cnt = word.count(i)     # word.count(H) // word에서 H의 개수
    cnt_list.append(cnt)    # 배열에 추가

    
if cnt_list.count(max(cnt_list)) > 1 :   # 최대개수가 2개 이상이면
    print('?')
else: 
    max_index = cnt_list.index(max(cnt_list))    # 최대개수 단어의 인덱스
    print(word2[max_index])                      
    
    
