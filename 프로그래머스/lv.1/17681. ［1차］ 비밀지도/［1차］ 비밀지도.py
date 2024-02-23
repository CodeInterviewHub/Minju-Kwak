def solution(n, arr1, arr2):
    answer = []
    ans = ''
    for na in range(n):
        # 이진수로 변환하고 0으로 채우기
        narr1 = format(arr1[na], 'b').zfill(n)
        narr2 = format(arr2[na], 'b').zfill(n)
        for i in range(n):
            if narr1[i] == '1' or narr2[i] == '1':
                ans += '#'
            else:
                ans += ' '
        answer.append(ans)
        ans = ''
    return answer


#런타임에러
# def solution(n, arr1, arr2):
#     answer = []
#     narr1, narr2 = [],[]
#     ans = ''
#     for na in range(n):
#         while arr1[na] != 0 :
#             narr1.insert(0,arr1[na] % 2)
#             arr1[na] = arr1[na] // 2
#         if len(narr1) != n:
#             narr1.insert(0,0)
#         while arr2[na] != 0 :
#             narr2.insert(0,arr2[na] % 2)
#             arr2[na] = arr2[na] // 2
#         if len(narr2) != n:
#             for j in range(n-len(narr2)):
#                 narr2.insert(0,0)
#         for i in range(n):
#             if narr1[i] or narr2[i]:
#                 ans += '#'
#             else:
#                 ans += ' '
#         answer.append(ans)
#         narr1 = []
#         narr2 = []
#         ans = ''
#     return answer