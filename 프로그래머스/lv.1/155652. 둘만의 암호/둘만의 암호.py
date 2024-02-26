def solution(s, skip, index):
    answer = ''
    
    alpha = [chr(i) for i in range(97, 123)]
    for i in skip:
        alpha.remove(i)
    
    for _s in s:
        idx = alpha.index(_s) + index
        answer += alpha[idx % len(alpha)]
        
    return answer