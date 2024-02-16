def solution(number, limit, power):
    divisor = []
    
    for n in range(1,number+1):
        count = 0
        for i in range(1,int(n**(1/2))+1):
            if n%i == 0:
                count +=1
                if i**2 != n:
                    count +=1
            if count > limit:
                # answer += power
                count = power
                break
        # answer += count
        divisor.append(count)
    
    # return answer
    return sum(divisor)