import collections

def solution(genres, plays):
    answer = []
    data = collections.defaultdict(int)
    count = collections.defaultdict(list)
    for i in range(len(genres)):
        data[genres[i]] +=plays[i]
        count[genres[i]].append([plays[i],i])
    data = sorted(data.items(), key=lambda v:-v[1])
    for a,b in data:
        target = sorted(count[a], key=lambda v:-v[0])
        if len(target) == 1:
            answer.append(target[0][1])
            continue
        for i in range(2):
            answer.append(target[i][1])
    return answer