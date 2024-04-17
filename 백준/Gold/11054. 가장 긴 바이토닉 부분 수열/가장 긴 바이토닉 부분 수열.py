import sys

n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))

increase = []
increase2 = []
for i in data:
    increase.append([i])

for i in range(n):
    for j in range(i):
        if data[j] < data[i]:
            if len(increase[j]) + 1 > len(increase[i]):
                increase[i] = increase[j] + [data[i]]
data.reverse()
for i in data:
    increase2.append([i])
for i in range(n):
    for j in range(i):
        if data[j] < data[i]:
            if len(increase2[j]) + 1 > len(increase2[i]):
                increase2[i] = increase2[j] + [data[i]]

answer = 0
for i in range(n):
    temp = len(increase[i]) + len(increase2[n - i - 1]) - 1
    answer = max(answer, temp)

print(answer)