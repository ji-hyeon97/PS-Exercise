import collections

def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    reportHash = collections.defaultdict(list)
    stop = collections.defaultdict(int)
    
    for i in report:
        first, second = i.split(" ")
        reportHash[first].append(second)
    
    for i in id_list:
        for target in reportHash[i]:
            stop[target] +=1
    
    for i in id_list:
        cnt = 0
        for target in reportHash[i]:
            if stop[target] >= k:
                cnt+=1
        answer.append(cnt)
    
    return answer