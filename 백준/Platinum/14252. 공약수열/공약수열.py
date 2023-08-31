import sys
import math

n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))
data.sort()
answer = 0

for i in range(len(data) - 1):
    if math.gcd(data[i], data[i + 1]) == 1:
        continue
    flag = 1
    for j in range(data[i] + 1, data[i + 1]):
        if math.gcd(data[i], j) == 1 and math.gcd(math.gcd(data[i + 1], j)) == 1:
            answer += 1
            flag = 0
            break
    if flag == 1:
        answer += 2
print(answer)