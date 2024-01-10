import sys
import heapq
import collections

n = int(sys.stdin.readline().rstrip())
data = []
cnt = collections.defaultdict(int)

for _ in range(n):
    t = int(sys.stdin.readline().rstrip())

    if t != 0:
        cnt[t]+=1
        heapq.heappush(data,abs(t))
    else:
        if len(data) == 0:
            print(0)
        else:
            temp = heapq.heappop(data)
            if -1*temp in cnt:
                print(-1*temp)
                cnt[-1*temp]-=1
                if cnt[-1*temp] == 0:
                    del cnt[-1*temp]
                continue
            if temp in cnt:
                print(temp)
                cnt[temp] -= 1
                if cnt[temp] == 0:
                    del cnt[temp]