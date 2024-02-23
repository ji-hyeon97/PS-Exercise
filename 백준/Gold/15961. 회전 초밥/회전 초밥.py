import sys
from collections import deque

n, d, k, c = map(int, sys.stdin.readline().split())
queue = []

for _ in range(n):
    t = int(sys.stdin.readline().rstrip())
    queue.append(t)

take = deque()
result = 0
cnt = -1
check = [0 for _ in range(d + 1)]
count = 0
while True:
    cnt += 1
    if cnt > n+k:
        break
    take.append(queue[(cnt % n)])
    if check[queue[(cnt % n)]] == 0:
        count += 1
        check[queue[(cnt % n)]] += 1
    else:
        check[queue[(cnt % n)]] += 1

    if len(take) == k:
        if check[c] != 0:
            answer = count
        else:
            answer = count + 1
        result = max(result, answer)
        temp = take.popleft()
        if check[temp] == 1:
            count -= 1
        check[temp] -= 1

print(result)