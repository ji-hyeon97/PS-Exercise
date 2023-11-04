import sys
import heapq

data = []
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if len(data)==0:
            print(0)
        else:
            target = heapq.heappop(data)
            print(-1*target)
    else:
        heapq.heappush(data,-1*x)