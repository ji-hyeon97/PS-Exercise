from collections import deque

T = int(input().rstrip())
for t in range(1, T + 1):
    K = int(input().rstrip())
    wheel1 = deque(list(map(int, input().split())))
    wheel2 = deque(list(map(int, input().split())))
    wheel3 = deque(list(map(int, input().split())))
    wheel4 = deque(list(map(int, input().split())))

    for _ in range(K):
        a, b = map(int, input().split())
        graph = [0 for _ in range(5)]
        if a == 1:
            graph[1] = 1
            if wheel1[2] != wheel2[6]:
                graph[2] = 1
                if wheel2[2] != wheel3[6]:
                    graph[3] = 1
                    if wheel3[2] != wheel4[6]:
                        graph[4] = 1

            for i in range(1, 5):
                if i == 1 and graph[i] == 1:
                    if b == 1:
                        temp = wheel1.pop()
                        wheel1.appendleft(temp)
                    else:
                        temp = wheel1.popleft()
                        wheel1.append(temp)
                if i == 2 and graph[i] == 1:
                    if b == 1:
                        temp = wheel2.popleft()
                        wheel2.append(temp)
                    else:
                        temp = wheel2.pop()
                        wheel2.appendleft(temp)
                if i == 3 and graph[i] == 1:
                    if b == 1:
                        temp = wheel3.pop()
                        wheel3.appendleft(temp)
                    else:
                        temp = wheel3.popleft()
                        wheel3.append(temp)
                if i == 4 and graph[i] == 1:
                    if b == 1:
                        temp = wheel4.popleft()
                        wheel4.append(temp)
                    else:
                        temp = wheel4.pop()
                        wheel4.appendleft(temp)
        if a == 2:
            graph[2] = 1
            if wheel2[2] != wheel3[6]:
                graph[3] = 1
                if wheel3[2] != wheel4[6]:
                    graph[4] = 1
            if wheel1[2] != wheel2[6]:
                graph[1] = 1

            for i in range(1, 5):
                if i == 2 and graph[i] == 1:
                    if b == 1:
                        temp = wheel2.pop()
                        wheel2.appendleft(temp)
                    else:
                        temp = wheel2.popleft()
                        wheel2.append(temp)
                if i == 1 and graph[i] == 1:
                    if b == 1:
                        temp = wheel1.popleft()
                        wheel1.append(temp)
                    else:
                        temp = wheel1.pop()
                        wheel1.appendleft(temp)
                if i == 3 and graph[i] == 1:
                    if b == 1:
                        temp = wheel3.popleft()
                        wheel3.append(temp)
                    else:
                        temp = wheel3.pop()
                        wheel3.appendleft(temp)
                if i == 4 and graph[i] == 1:
                    if b == 1:
                        temp = wheel4.pop()
                        wheel4.appendleft(temp)
                    else:
                        temp = wheel4.popleft()
                        wheel4.append(temp)
        if a == 3:
            graph[3] = 1
            if wheel3[2] != wheel4[6]:
                graph[4] = 1
            if wheel2[2] != wheel3[6]:
                graph[2] = 1
                if wheel1[2] != wheel2[6]:
                    graph[1] = 1

            for i in range(1, 5):
                if i == 3 and graph[i] == 1:
                    if b == 1:
                        temp = wheel3.pop()
                        wheel3.appendleft(temp)
                    else:
                        temp = wheel3.popleft()
                        wheel3.append(temp)
                if i == 4 and graph[i] == 1:
                    if b == 1:
                        temp = wheel4.popleft()
                        wheel4.append(temp)
                    else:
                        temp = wheel4.pop()
                        wheel4.appendleft(temp)
                if i == 2 and graph[i] == 1:
                    if b == 1:
                        temp = wheel2.popleft()
                        wheel2.append(temp)
                    else:
                        temp = wheel2.pop()
                        wheel2.appendleft(temp)
                if i == 1 and graph[i] == 1:
                    if b == 1:
                        temp = wheel1.pop()
                        wheel1.appendleft(temp)
                    else:
                        temp = wheel1.popleft()
                        wheel1.append(temp)
        if a == 4:
            graph[4] = 1
            if wheel3[2] != wheel4[6]:
                graph[3] = 1
                if wheel2[2] != wheel3[6]:
                    graph[2] = 1
                    if wheel1[2] != wheel2[6]:
                        graph[1] = 1

            for i in range(1, 5):
                if i == 4 and graph[i] == 1:
                    if b == 1:
                        temp = wheel4.pop()
                        wheel4.appendleft(temp)
                    else:
                        temp = wheel4.popleft()
                        wheel4.append(temp)
                if i == 3 and graph[i] == 1:
                    if b == 1:
                        temp = wheel3.popleft()
                        wheel3.append(temp)
                    else:
                        temp = wheel3.pop()
                        wheel3.appendleft(temp)
                if i == 2 and graph[i] == 1:
                    if b == 1:
                        temp = wheel2.pop()
                        wheel2.appendleft(temp)
                    else:
                        temp = wheel2.popleft()
                        wheel2.append(temp)
                if i == 1 and graph[i] == 1:
                    if b == 1:
                        temp = wheel1.popleft()
                        wheel1.append(temp)
                    else:
                        temp = wheel1.pop()
                        wheel1.appendleft(temp)

    answer = 1*wheel1[0] + 2*wheel2[0] + 4*wheel3[0] + 8*wheel4[0]

    print("#"+str(t)+" "+str(answer))