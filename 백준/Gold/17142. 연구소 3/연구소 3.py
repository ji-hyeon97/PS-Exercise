from collections import deque


def bfs(tlst):
    q = deque()
    v = [[0] * N for _ in range(N)]

    for ti, tj in tlst:
        q.append((ti, tj))
        v[ti][tj] = 1

    cnt = CNT
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and arr[ni][nj] != 1:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
                if arr[ni][nj] == 0:
                    cnt -= 1
                    if cnt == 0:
                        return v[ni][nj] - 1

    return N * N


def dfs(n, s, tlst):
    global ans
    if n == M:
        ans = min(ans, bfs(tlst))
        return

    for j in range(s, VCNT):
        dfs(n + 1, j + 1, tlst + [vlst[j]])


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

CNT = 0
vlst = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            CNT += 1
        elif arr[i][j] == 2:
            vlst.append((i, j))
VCNT = len(vlst)

if CNT == 0:
    ans = 0
else:
    ans = N * N
    dfs(0, 0, [])
    if ans == N * N:
        ans = -1
print(ans)