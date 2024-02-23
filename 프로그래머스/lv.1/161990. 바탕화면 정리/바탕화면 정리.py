def solution(wallpaper):
    answer = [0,0,0,0]
    sh, sw , eh, ew =[],[],[],[]
    for h in range(len(wallpaper)):
        for w in range(len(wallpaper[0])):
            if wallpaper[h][w] == '#':
                sh.append(h)
                sw.append(w)
                eh.append(h+1)
                ew.append(w+1)
                
    return [min(sh),min(sw),max(eh),max(ew)]