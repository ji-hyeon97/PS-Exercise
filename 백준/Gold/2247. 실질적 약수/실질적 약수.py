import sys

n = int(sys.stdin.readline().rstrip())
answer = 0

for i in range(2, (n // 2) + 1):
    answer += (int(n / i) - 1) * i
print(answer%1000000)