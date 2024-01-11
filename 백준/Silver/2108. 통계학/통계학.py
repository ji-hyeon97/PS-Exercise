import sys
import collections

n = int(sys.stdin.readline().rstrip())
data = []

for _ in range(n):
    k = int(sys.stdin.readline().rstrip())
    data.append(k)

data.sort()
print(round(sum(data) / n))
print(data[n // 2])

dic = collections.defaultdict(int)
for i in data:
    dic[i] += 1
temp = sorted(dic.items(), key=lambda v:v[1], reverse=True)
tmp = temp[0][1]
answer = []
for a,b in temp:
    if b != tmp:
        break
    answer.append(a)
if len(answer) == 1:
    print(answer[0])
else:
    answer.sort()
    print(answer[1])
print(data[-1] - data[0])