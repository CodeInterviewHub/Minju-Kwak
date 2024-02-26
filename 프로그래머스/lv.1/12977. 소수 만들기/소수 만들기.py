import itertools

def solution(nums):
    answer = []
    result = list(itertools.combinations(nums,3))
    for res in result:
        chk = 0
        for s in range(2,sum(res)):
            if sum(res) % s == 0:
                chk += 1
        if chk == 0 :
            answer.append(sum(res))
    return len(answer)