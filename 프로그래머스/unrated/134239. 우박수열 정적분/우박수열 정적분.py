def solution(k, ranges):
    answer = [k]
    dic = {}
    result = []
    while True:
        if k == 1:
            break
        if k%2 == 0:
            k = k//2
            answer.append(k)
        else:
            k = 3*k+1
            answer.append(k)
    for i in range(len(answer)-1):
        dic[i] = min(answer[i],answer[i+1]) + 0.5*abs(answer[i]-answer[i+1])
    for data in ranges:
        start = data[0]
        end = data[1] + len(dic)
        if start > end:
            result.append(-1.0)
            continue
        if start == end:
            result.append(0)
            continue
        width = 0
        for i in range(start,end):
            width+=dic[i]
        result.append(width)
    return result