import sys

T = int(sys.stdin.readline().rstrip())

data = [1 for _ in range(104)]
data[0] = 1
data[1] = 1
data[2] = 1
data[3] = 2
data[4] = 2

for i in range(5, 104):
    data[i] = data[i-2] + data[i-3]

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    print(data[n-1])