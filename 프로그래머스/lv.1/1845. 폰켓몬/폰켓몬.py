def solution(nums):
    check = len(nums) // 2
    if len(list(set(nums))) <= check:
        return len(list(set(nums)))
    else:
        return check