def solution(n, m, section):
    answer = 0
    bak = []
    sec = 0
    # 타임에러
    # for b in range(n):
    #     if b+1 in section:
    #         bak.append(0)
    #     else:
    #         bak.append(1)
    # for s in section:
    #     if bak[s-1] == 0:
    #         bak[s-1: s - 1 + m] = [1 for s in range(m)]
    #         answer += 1
    for s in range(len(section)):
        if section[s] >= sec:
            sec = section[s]
            sec += m
            answer+=1
        else:
            pass
    return answer