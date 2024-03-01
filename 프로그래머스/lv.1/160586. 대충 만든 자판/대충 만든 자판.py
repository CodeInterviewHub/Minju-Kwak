def solution(keymap, targets):
    answer = []
    
    for target in targets:
        ntart = 0
        for tar in target:
            k=[]
            for key in keymap:
                if tar in key:
                    k.append(list(key).index(tar)+1)
            if len(k) != 0:
                ntart += min(k)
            else:
                ntart = -1
                break
        answer.append(ntart)
    return answer