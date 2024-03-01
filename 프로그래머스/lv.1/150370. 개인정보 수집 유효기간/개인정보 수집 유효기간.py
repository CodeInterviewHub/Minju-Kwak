def solution(today, terms, privacies):
    result = []
    num = 0
    for p in privacies:
        privacy = p.split(" ")
        num += 1
        for t in terms:
            t = t.split(" ")
            if privacy[1] == t[0]:
                p = privacy[0].split(".")
                p[1] = str(int(p[1]) + int(t[1]))
                if int(p[1]) > 12:
                    if (int(p[1]) % 12) == 0:
                        print("==")
                        p[0] = str(int(p[0])+(int(p[1]) // 12)-1)
                        p[1] = "12"
                    else :
                        p[0] = str(int(p[0])+(int(p[1]) // 12))
                        p[1] = str((int(p[1]) % 12))
                    print(p)
                day = today.split(".")
                if int(day[0]) > int(p[0]):
                    result.append(num)
                elif int(day[0]) == int(p[0]):
                    if int(day[1]) > int(p[1]):
                        result.append(num)
                    elif int(day[1]) == int(p[1]):
                        if int(day[2]) >= int(p[2]):
                            result.append(num)
    return result