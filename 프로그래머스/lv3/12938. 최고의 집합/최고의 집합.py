def solution(n, s):
    answer = []
    if n>s:
        return[-1]
    data = s//n
    plus = s%n
    for _ in range(n):
        answer.append(data)
    if plus != 0:
        for i in range(n-1,n-plus-1,-1):
            answer[i]+=1       
    return answer