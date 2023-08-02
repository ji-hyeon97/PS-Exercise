from collections import deque

def solution(n, t, m, p):
    answer = ''
    data = deque()
    for i in range(t*m):
        temp = ''
        if i == 0:
            data.append(str(i))
            continue
        while True:
            if i == 0:
                break
            value = str(i%n)
            if value == '10':
                value = 'A'
            if value == '11':
                value = 'B'
            if value == '12':
                value = 'C'
            if value == '13':
                value = 'D'
            if value == '14':
                value = 'E'
            if value == '15':
                value = 'F'
            temp+=value
            i = int(i/n)
        for j in range(len(temp)-1,-1,-1):
            data.append(temp[j])
    for i in range(p-1,len(data),m):
        if len(answer) == t:
            break
        answer+=data[i]
    return answer