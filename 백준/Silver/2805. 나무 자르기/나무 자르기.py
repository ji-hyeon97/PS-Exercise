import sys

n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

s = 1
e = max(data)

while s <= e:
    mid = (s + e) // 2
    temp = 0
    for i in data:
        if i >= mid:
            temp += (i - mid)
    if temp < m:
        e = mid - 1
    else:
        s = mid + 1
print(e)