def solution(s):
    answer = ''
    cnt = 0
    
    for word in s:
        if word == " ":
            answer += word
            cnt = 0
        elif cnt % 2 == 0:
            answer += word.upper()
            cnt += 1
        else:
            answer += word.lower()
            cnt += 1
        
            
    return answer