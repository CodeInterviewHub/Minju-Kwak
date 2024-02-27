def solution(s):
    answer = []
    old = []
    for sa in s:
        if sa in old:
            old.append(sa)
            idx = list(filter(lambda x: old[x] == sa, range(len(old)))) 
            answer.append(idx[-1] - idx[-2])
        else:
            old.append(sa)
            answer.append(-1)
    return answer