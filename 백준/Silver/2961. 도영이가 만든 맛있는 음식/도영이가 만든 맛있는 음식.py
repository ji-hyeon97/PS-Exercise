import sys

n = int(sys.stdin.readline().rstrip())
element = []
for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    element.append(data)

answer = int(1e9)


def recur(idx, sin, sen, flag):
    global answer
    if idx == n:
        if flag == 0:
            return
        answer = min(answer, abs(sin - sen))
        return
    recur(idx + 1, sin * element[idx][0], sen + element[idx][1], flag + 1)
    recur(idx + 1, sin, sen, flag)


recur(0, 1, 0, 0)
print(answer)