def solution(lottos, win_nums):
    answer = []
    cor = len(list(set(lottos) & set(win_nums)))
    print(lottos.count(0))
    print(cor)
    if lottos.count(0) + cor == 0:
        answer.append(6)
    else:
        answer.append((7 - lottos.count(0) - cor))
    if cor == 0 :
        answer.append(6)
    else:
        answer.append(7-cor)
    return answer