def solution(ingredient):
    answer = 0
    ing = []
    for i in ingredient:
        ing.append(i)
        if ing[-4:] == [1,2,3,1]:
            answer += 1
            del ing[-4:]
    
    # f = 0
    # f = ''.join(str(s) for s in ingredient)
    # while f.find('1231'):
    #     s = f.find('1231')
    #     if s == -1:
    #         break
    #     else:
    #         f = f[:s] + f[s+4:]
    #         answer += 1
            
    return answer