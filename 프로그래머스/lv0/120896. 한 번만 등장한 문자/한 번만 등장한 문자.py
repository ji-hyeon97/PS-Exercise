from collections import Counter

def solution(s):
    answer = ''
    data = Counter(s)
    target = []
    for i in data:
        if data[i] == 1:
            target.append(i)
    target.sort()
    answer = "".join(target)
    return answer