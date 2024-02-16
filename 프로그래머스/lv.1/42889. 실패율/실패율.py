def solution(N, stages):
    answer = []
    nclear = [0 for n in range(N)]
    arv = [0 for n in range(N)]
    for s in stages:
        if s <= N:
            nclear[s-1] += 1
            for i in range(s):
                arv[i] += 1
        if s > N:
            for i in range(s-1):
                arv[i] += 1
    for j in range(1,N+1):
        if nclear[j-1] == 0:
            answer.append([0,j])
        else:
            answer.append([nclear[j-1]/arv[j-1],j])
    answer.sort(key = lambda x : x[0],reverse=True)

    nanswer = [answer[n][1] for n in range(N)]
    return nanswer