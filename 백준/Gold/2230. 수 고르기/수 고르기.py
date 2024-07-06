import sys

N, M = map(int, sys.stdin.readline().split())
data = []

for _ in range(N):
    data.append(int(sys.stdin.readline().rstrip()))

data.sort()

left = 0
right = 0
answer = data[-1] - data[0]

while right <= len(data) - 1 and left <= len(data) - 1:
    if data[right] - data[left] >= M:
        answer = min(answer, data[right] - data[left])
        left += 1
    else:
        right += 1

print(answer)