def solution(strings, n):
    answer = []
    string = []
    for s in strings:
        string.append(s[n]+s)
        
    string.sort()
    
    for g in string:
        answer.append(g[1:])
        
    return answer