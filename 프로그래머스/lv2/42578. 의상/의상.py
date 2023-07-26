import collections
def solution(clothes):
    answer = 1
    dic = collections.defaultdict(list)
    for data in clothes:
        dic[data[1]].append(data[0])
    if len(dic) == 1:
        answer = len(dic[clothes[0][1]])
        return answer
    for i in dic:
        answer = answer * (len(dic[i])+1)
    return answer-1