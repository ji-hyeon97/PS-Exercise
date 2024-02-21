import sys

N, M = map(int, sys.stdin.readline().split())
graph = [[6] * (M + 2)] + [[6] + list(map(int, sys.stdin.readline().split())) + [6] for _ in range(N)] + [[6] * (M + 2)]

lst = []
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if 1 <= graph[i][j] <= 5:
            lst.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cctv = [[], [1], [1, 3], [0, 1], [0, 1, 3], [0, 1, 2, 3]]


def cal(tlst):
    check = [[0] * (M + 2) for _ in range(N + 2)]
    for i in range(CNT):
        si, sj = lst[i]
        rot = tlst[i]
        type = graph[si][sj]
        for dr in cctv[type]:
            dr = (dr + rot) % 4
            ci, cj = si, sj
            while True:
                ci, cj = ci + dx[dr], cj + dy[dr]
                if graph[ci][cj] == 6:  # 벽이면 그만 뻗어감
                    break
                check[ci][cj] = 1

    cnt = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if graph[i][j] == 0 and check[i][j] == 0:
                cnt += 1
    return cnt


def dfs(n, tlst):
    global ans
    if n == CNT:
        ans = min(ans, cal(tlst))
        return

    dfs(n + 1, tlst + [0])
    dfs(n + 1, tlst + [1])
    dfs(n + 1, tlst + [2])
    dfs(n + 1, tlst + [3])


CNT = len(lst)
ans = N * M
dfs(0, [])
print(ans)