from collections import deque

for test_case in range(1, 11):
    n = int(input().rstrip())
    data = input().rstrip()
    queue = deque()
    for i in data:
        if i == "(":
            queue.append(i)
        if i == "[":
            queue.append(i)
        if i == "{":
            queue.append(i)
        if i == "<":
            queue.append(i)
        if i == "}":
            if len(queue) == 0:
                queue.append(i)
            else:
                if queue[-1] == "{":
                    queue.pop()
                else:
                    queue.append(i)
        if i == "]":
            if len(queue) == 0:
                queue.append(i)
            else:
                if queue[-1] == "[":
                    queue.pop()
                else:
                    queue.append(i)
        if i == ")":
            if len(queue) == 0:
                queue.append(i)
            else:
                if queue[-1] == "(":
                    queue.pop()
                else:
                    queue.append(i)
        if i == ">":
            if len(queue) == 0:
                queue.append(i)
            else:
                if queue[-1] == "<":
                    queue.pop()
                else:
                    queue.append(i)
    if len(queue) == 0:
        print("#" + str(test_case) + " " + str(1))
    else:
        print("#" + str(test_case) + " " + str(0))