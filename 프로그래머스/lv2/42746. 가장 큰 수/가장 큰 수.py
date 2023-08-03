import collections
def solution(numbers):
    answer = ''
    data = []
    for i in numbers:
        data.append(str(i))
    num = set()
    dic = collections.defaultdict(list)
    cnt = 0
    for i in data:
        while True:
            if len(i) >= 4:
                i = i[:4]
                break
            i+=i            
        dic[i].append(cnt)
        cnt+=1
        num.add(i)
    num = list(num)
    num.sort(reverse=True)
    for i in num:
        for j in dic[i]:
            answer+=data[j]
    if int(answer) == 0:
        return '0'
    return answer