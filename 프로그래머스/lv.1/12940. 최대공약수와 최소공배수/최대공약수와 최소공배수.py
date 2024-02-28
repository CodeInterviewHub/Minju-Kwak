def solution(n, m):
    answer =[0,m*n]
    nx = []
    mx = []
    # for na in range(n,0,-1):
    #     if n % na == 0:
    #         nx.append(n // na)
    # for ma in range(m,0,-1):
    #     if m % ma == 0:
    #         mx.append(m // ma)
    # answer.append(list(set(nx) & set(mx))[-1])
    while n != 0:
        a = m % n
        m = n
        n = a
    answer[0] = m
    answer[1] = (answer[1] // answer[0])
    return answer