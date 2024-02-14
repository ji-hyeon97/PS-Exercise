import sys

n = int(sys.stdin.readline().rstrip())
answer = 0

v1 = [0] * n
v2 = [0] * (2 * n)
v3 = [0] * (2 * n)


def dfs(depth):
    global answer
    if depth == n:
        answer += 1
        return
    for i in range(n):
        if v1[i] == v2[i + depth] == v3[depth - i] == 0:
            v1[i] = v2[i + depth] = v3[depth - i] = 1
            dfs(depth + 1)
            v1[i] = v2[i + depth] = v3[depth - i] = 0


dfs(0)
print(answer)