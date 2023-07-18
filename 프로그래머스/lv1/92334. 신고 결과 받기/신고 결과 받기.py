import collections

def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    
    reportHash = collections.defaultdict(list)
    stopped = collections.defaultdict(int)
    
    for i in report:
        data = i.split(" ")
        reportHash[data[0]].append(data[1])
        stopped[data[1]]+=1
        
    for i in id_list:
        mail = 0
        for j in reportHash[i]:
            if stopped[j] >=k:
                mail+=1
        answer.append(mail)

    return answer