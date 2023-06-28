def solution(n):
    answer = []
    data = str(n)
    for i in range(len(data)):
        answer.append(int(data[len(data)-i-1]))
    return answer