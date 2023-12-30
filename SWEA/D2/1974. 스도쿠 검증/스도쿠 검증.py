T = int(input())
for test_case in range(1, T + 1):
    graph = []
    flag = 0
    for _ in range(9):
        temp = list(map(int, input().split()))
        graph.append(temp)
        if len(set(temp)) != 9 and flag == 0:
            print("#" + str(test_case) + " 0")
            flag = 1
    if flag == 1:
        continue
    for i in range(9):
        temp = []
        for j in range(9):
            temp.append(graph[j][i])
        if len(set(temp)) != 9:
            print("#" + str(test_case) + " 0")
            flag = 1
            break
    if flag == 1:
        continue
    for i in range(0, 9, 3):
        if flag == 1:
            break
        for j in range(0, 9, 3):
            temp = 0
            for k in range(3):
                for l in range(3):
                    temp += graph[i + k][j + l]
            if temp != 45:
                print("#" + str(test_case) + " 0")
                flag = 1
                break
    if flag == 0:
        print("#" + str(test_case) + " 1")