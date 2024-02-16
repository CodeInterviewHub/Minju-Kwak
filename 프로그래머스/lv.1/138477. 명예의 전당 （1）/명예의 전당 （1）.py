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