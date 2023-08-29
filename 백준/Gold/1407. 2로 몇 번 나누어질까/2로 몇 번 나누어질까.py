import sys

a, b = map(int, sys.stdin.readline().split())
answer = 0

a = a - 1
resultA = 0
resultB = 0
resultA += (int(a) + 1)
resultB += (int(b) + 1)

data = []
two = 1
while True:
    two = two * 2
    if two > b:
        break
    data.append(two)

for i in range(len(data)):
    resultA += int(a / data[i]) * (2**i)
    resultB += int(b / data[i]) * (2**i)
print(resultB-resultA)