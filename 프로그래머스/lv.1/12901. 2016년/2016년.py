def solution(a, b):
    answer = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    day = 0
    day = (sum(month[:a]) + b) % 7 
    # for m in range(1, a):
    #     if m % 2 == 0:
    #         if m == 2:
    #             day += 29
    #         else:
    #             day += 30
    #     else:
    #         day += 31 
    # day = (day + b) % 7

    return answer[day]