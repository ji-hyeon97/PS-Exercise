import sys

n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))

lis = [data[0]]


def lowerBound(target):
    left = 0
    right = len(lis) - 1
    mid = (left + right) // 2

    if lis[right] < target:
        return -1

    if lis[left] >= target:
        return 0

    while left + 1 < right:
        if lis[mid] < target:
            left = mid
        else:
            right = mid
        mid = (left + right) // 2
    return right


for i in range(1, n):
    index = lowerBound(data[i])
    if index == -1:
        lis.append(data[i])
        continue
    lis[index] = data[i]

print(len(lis))