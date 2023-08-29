import sys
import collections
import math

a, b = map(int, sys.stdin.readline().split())
data = b // a
dic = collections.defaultdict(list)

for i in range(2, int(math.sqrt(data)) + 2):
    if data % i == 0 and math.gcd(i, data // i) == 1:
        dic[i + (data // i)] = [i, (data // i)]

if len(dic) == 0:
    dic[1 + data] = [1, data]

dic = sorted(dic.items())
left = min(dic[0][1])
right = max(dic[0][1])
print(left * a, right * a)