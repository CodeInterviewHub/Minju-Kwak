def solution(food):
    forward=''
    answer = ''
    cal = 0
    
    for f in food:
        if f//2 != 0:
            for n in range(0,f//2):
                forward += str(cal)
        cal += 1
        
    answer = forward + "0"
    
    for a in forward[::-1]:
        answer += a
    
    return answer