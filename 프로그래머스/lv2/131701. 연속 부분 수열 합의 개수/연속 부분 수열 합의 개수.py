def solution(elements):
    answer = []
    n = len(elements)
    elements = elements + elements
    
    for i in range(1,n+1):
        for j in range(n):
            data =sum(elements[j:(j+i)])
            answer.append(data)
    
    return len(list(set(answer)))