import sys

n = int(sys.stdin.readline().rstrip())
data = list(map(str, sys.stdin.readline().rstrip()))

answer = 0
for i in range(len(data)):
    answer += (ord(data[i]) - 96) * (31 ** i)
print(answer)