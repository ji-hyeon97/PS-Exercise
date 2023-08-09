from collections import deque

def solution(order):
    answer = 0
    order = deque(order)
    stack = deque(i for i in range(1,max(order)+1))
    wait = []
    for i in order:
        flag = 0
        if len(wait) != 0:
            if wait[-1] == i:
                wait.pop()
                answer+=1
                flag = 1
                continue
        if i == stack[0]:
            stack.popleft()
            answer+=1
            flag = 1
            continue
        else:
            while True:
                if len(stack) == 1:
                    break
                data = stack.popleft()
                wait.append(data)
                if stack[0] == i:
                    stack.popleft()
                    answer+=1
                    flag = 1
                    break
        if flag == 0:
            return answer
    return answer