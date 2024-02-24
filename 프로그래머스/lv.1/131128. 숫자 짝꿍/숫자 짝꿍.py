def solution(X, Y):
    answer = ''
    xcnt = 0
    ycnt = 0
    
    for i in range(9,-1,-1):
        xcnt = X.count(str(i))
        ycnt = Y.count(str(i))
        if xcnt !=0 and ycnt != 0:
            if i == 0 and len(answer) == 0:
                return "0"
            else:
                answer += str(i) * xcnt if xcnt < ycnt else str(i) * ycnt
    if answer == '':
        return "-1"
    else:
        return answer
    
#테스트11-15 시간 초과
def solution(X, Y):
    answer = ''
    ans = []
    xlist = list(X)
    ylist = list(Y)
    for x in xlist:
        for j, y in enumerate(ylist):
            if x == y :
                ans.append(x)
                del ylist[j]
                break
            
    if ans == []:
        return "-1"
    else:
        answer = str(int(''.join(s for s in sorted(ans,reverse = True))))
        return answer
