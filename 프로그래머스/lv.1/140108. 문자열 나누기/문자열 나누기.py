def solution(s):
    answer = 0
    chk = []
    start = ''
    snum, dnum = 0, 0
    
    for sa in s:
        if len(chk) == 0:
            start = sa
        chk.append(sa)
        if sa == start:
            snum += 1
        else:
            dnum += 1
        if snum == dnum:
            answer += 1
            chk = []
            snum , dnum = 0, 0
    if len(chk) != 0:
        answer += 1 
    return answer