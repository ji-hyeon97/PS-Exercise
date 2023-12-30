T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    data = list(map(int, input().split()))
    answer = int(1e9)
    companyX = data[0]
    companyY = data[1]
    homeX = data[2]
    homeY = data[3]
    client = []
    for i in range(4, len(data) - 1, 2):
        client.append([data[i], data[i + 1]])
    visit = [0 for _ in range(n + 5)]


    def dfs(distance, cnt, x, y):
        global answer
        global n
        if cnt == n:
            distance = distance + abs(homeX - x) + abs(homeY - y)
            answer = min(distance, answer)

        for i in range(n):
            if visit[i] == 0:
                visit[i] = 1
                dfs(distance+abs(x - client[i][0]) + abs(y - client[i][1]), cnt + 1, client[i][0], client[i][1])
                visit[i] = 0


    for i in range(n):
        if visit[i] == 0:
            visit[i] = 1
            dfs(abs(companyX - client[i][0]) + abs(companyY - client[i][1]), 1, client[i][0], client[i][1])
            visit[i] = 0
    print("#"+str(test_case)+" "+str(answer))