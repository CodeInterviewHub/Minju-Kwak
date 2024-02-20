def solution(d, budget):
    answer = 0
    nd = []
    for ds in sorted(d):
        nd.append(ds)
        if sum(nd) <= budget:
            answer = len(nd)
        else:
            return answer
        
    return answer