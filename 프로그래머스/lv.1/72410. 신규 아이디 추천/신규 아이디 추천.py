def solution(new_id):
    oid = []
    #1
    new_id = new_id.lower()
    #2/3
    for n in new_id:
        if (n.isalpha() or n.isdigit() or n == '.' or n == '-' or n == '_') == True:
            oid.append(n)
        if oid[-2:] == ['.', '.']:
            del oid[-1]
    #4
    if len(oid) > 0:
        if oid[0] == '.':
            del oid[0]
    if len(oid) > 0:
        if oid[-1] == '.':
            del oid[-1]
    #5
    if oid == []:
        oid.append('a')
    #6
    if len(oid) >= 16:
        oid = oid[:15]
        if oid[-1] == '.':
            del oid[-1]
    #7
    if len(oid) <= 2:
        for i in range(3-len(oid)):
            oid.append(oid[-1])
    return ''.join(o for o in oid)