import sys

n, k = map(int, sys.stdin.readline().split())

data = list(map(int, sys.stdin.readline().split()))
robot = [0] * n

answer = 0
while True:
    answer += 1

    data = [data[-1]] + data[:-1]
    robot = [0] + robot[:-1]
    robot[n - 1] = 0

    for i in range(n - 2, 0, -1):
        if robot[i] == 1 and robot[i + 1] == 0 and data[i + 1] > 0:
            robot[i], robot[i + 1] = 0, 1
            data[i + 1] -= 1

    if data[0] > 0:
        robot[0] = 1
        data[0] -= 1

    if data.count(0) >= k:
        break
print(answer)