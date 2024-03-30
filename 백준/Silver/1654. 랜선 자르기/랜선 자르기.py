import sys

k, n = map(int, sys.stdin.readline().split())
lan = []
for _ in range(k):
    lan.append(int(sys.stdin.readline().rstrip()))
lan.sort()
start = 1
ends = lan[-1]
result = 0
while start <= ends:
    mid = (start + ends) // 2
    answer = 0
    for i in lan:
        answer += i // mid
    if answer >= n:
        result = max(result, mid)
        start = mid + 1
    else:
        ends = mid - 1

print(result)