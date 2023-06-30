def solution(X, Y):
    answer = ''
    left = [0 for _ in range(11)]
    right = [0 for _ in range(11)]
    target = []
    for i in X:
        left[int(i)]+=1
    for i in Y:
        right[int(i)]+=1
    for i in range(0,11):
        while(True):
            if left[i] == 0:
                break
            if right[i] == 0:
                break
            target.append(i)
            left[i] -=1
            right[i] -=1
    if len(target) == 0:
        answer = '-1'
    else:
        target.sort(reverse=True)
        for i in target:
            answer+=str(i)
        if answer[0] == '0':
            answer = '0'
    return answer