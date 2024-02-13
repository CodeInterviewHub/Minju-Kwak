# Test9 , Test11 런타임에러
def solution(k, score):
    answer = []
    total=[]
    for t in range(0,k):
        total.append(score[t])
        answer.append(min(total))
        
    del score[:k]
    
    for s in score:
        if min(total) < s:
            total.remove(min(total))
            total.append(s)
        answer.append(min(total))
    
    return answer

# 9번, 11번이 len(score) < k 인 케이스
def solution(k, score):
    answer = []
    total=[]
    
    if k > len(score):
        k = len(score)
        
    for t in range(0,k):
        total.append(score[t])
        answer.append(min(total))
        
    del score[:k]
    
    for s in score:
        if min(total) < s:
            total.remove(min(total))
            total.append(s)
        answer.append(min(total))
    
    return answer
