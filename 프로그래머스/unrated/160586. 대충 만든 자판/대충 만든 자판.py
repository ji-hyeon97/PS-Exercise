import collections

def solution(keymap, targets):
    answer = []
    dic = collections.defaultdict(int)
    
    for data in keymap:
        for i in range(len(data)):
            if data[i] not in dic:
                dic[data[i]] = i+1
            else:
                if i+1 < dic[data[i]]:
                    dic[data[i]] = i+1
    for data in targets:
        cnt = 0
        for i in data:
            if i not in dic:
                cnt = 0
                break
            else:
                cnt+=dic[i]
        if cnt == 0:
            answer.append(-1)
            continue
        answer.append(cnt)
    return answer