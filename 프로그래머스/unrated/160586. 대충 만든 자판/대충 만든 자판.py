def solution(keymap, targets):
    answer = []
    dic = {}
    for key in keymap:
        for i in range(len(key)):
            if key[i] not in dic:
                dic[key[i]] = i+1
            else:
                if dic[key[i]] > i+1:
                    dic[key[i]] = i+1
    for data in targets:
        result = 0
        flag = 1
        for i in data:
            if i not in dic:
                answer.append(-1)
                flag = 0
                break
            else:
                result+=dic[i]
        if flag ==1:
            answer.append(result)
    return answer