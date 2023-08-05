def solution(numbers):
    n = len(numbers)
    result = [-1] * n
    answer = []
    for i in range(n-2, -1, -1):
        j = i + 1
        while True:
            if j == -1 or numbers[i] < numbers[j]:
                break                
            j = result[j]
        result[i] = j
    for i in result:
        if i != -1:
            answer.append(numbers[i])
        else:
            answer.append(-1)
    return answer