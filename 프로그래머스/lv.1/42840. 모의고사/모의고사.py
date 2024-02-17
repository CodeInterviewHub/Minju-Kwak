def solution(answers):
    answer = [0,0,0]
    supoza1 = [1,2,3,4,5]
    supoza2 = [2,1,2,3,2,4,2,5]
    supoza3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for a, ans in enumerate(answers):
        if ans == supoza1[a % len(supoza1)]:
            answer[0] +=1
        if ans == supoza2[a % len(supoza2)]:
            answer[1] +=1
        if ans == supoza3[a % len(supoza3)]:
            answer[2] +=1
    
    return sorted([i+1 for i in range(len(answer)) if max(answer) == answer[i]])