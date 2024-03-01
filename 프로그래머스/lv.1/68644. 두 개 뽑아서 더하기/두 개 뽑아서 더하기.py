def solution(numbers):
    answer = []
    numbers.sort()
    for i,num in enumerate(numbers):
        for n in range(i+1,len(numbers)):
            answer.append(num + numbers[n])
            
    return sorted(list(set(answer)))