import collections

def solution(gems):
    answer = []
    k = len(set(gems))
    maxl = len(gems) + 100
    lt = 0
    data = collections.defaultdict(int)
    for rt in range(len(gems)):
        data[gems[rt]]+=1
        while len(data) == k:
            if rt-lt+1 < maxl:
                maxl = rt-lt+1
                answer = [lt+1,rt+1]
            data[gems[lt]]-=1
            if data[gems[lt]] == 0:
                del data[gems[lt]]
            lt+=1
    return answer