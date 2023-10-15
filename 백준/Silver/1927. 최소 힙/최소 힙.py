import sys
import heapq

n = int(sys.stdin.readline().rstrip())
data = []

for _ in range(n):
    a = int(sys.stdin.readline().rstrip())
    if a == 0:
        if len(data) == 0:
            print(0)
        else:
            print(heapq.heappop(data))
    else:
        heapq.heappush(data,a)