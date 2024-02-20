def solution(s):
    ans = ''
    alpha = ''
    for i in range(0,len(s)):
        if s[i].isdigit():
            ans += str(s[i])
        else:
            alpha += str(s[i])
            if alpha == 'one':
                ans += str(1)
                alpha = ''
            elif alpha == 'two':
                ans += str(2)
                alpha = ''
            elif alpha == 'three':
                ans += str(3)
                alpha = ''
            elif alpha == 'four':
                ans += str(4)
                alpha = ''
            elif alpha == 'five':
                ans += str(5)
                alpha = ''
            elif alpha == 'six':
                ans += str(6)
                alpha = ''
            elif alpha == 'seven':
                ans += str(7)
                alpha = ''
            elif alpha == 'eight':
                ans += str(8)
                alpha = ''
            elif alpha == 'nine':
                ans += str(9)
                alpha = ''
            elif alpha == 'zero':
                ans += str(0)
                alpha = ''
              
    return int(ans)