import sys
from collections import deque

queue = deque()

n, m = map(int, sys.stdin.readline().split())
data = list(map(str, sys.stdin.readline().rstrip()))
cnt = list(map(int, sys.stdin.readline().split()))
answer = 0
dic = {}
dic['A'] = 0
dic['C'] = 0
dic['G'] = 0
dic['T'] = 0

for i in range(len(data)+1):
    if len(queue) == m:
        if dic['A'] >= cnt[0] and dic['C'] >= cnt[1] and dic['G'] >= cnt[2] and dic['T'] >= cnt[3]:
            answer += 1
            dic[queue[0]] -= 1
            queue.popleft()
        else:
            dic[queue[0]] -= 1
            queue.popleft()
    if i == len(data):
        continue
    queue.append(data[i])
    dic[data[i]] += 1
print(answer)