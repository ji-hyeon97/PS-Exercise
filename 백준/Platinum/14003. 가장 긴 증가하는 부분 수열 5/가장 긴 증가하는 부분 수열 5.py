import sys

n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))

temp = [data[0]]
idx = [0]


def lowerBound(target):
    left = 0
    right = len(temp) - 1
    mid = (left + right) // 2

    if temp[right] < target:
        return -1
    if temp[left] >= target:
        return 0

    while left + 1 < right:
        if temp[mid] < target:
            left = mid
        else:
            right = mid
        mid = (left + right) // 2

    return right


for i in range(1, n):
    index = lowerBound(data[i])
    if index == -1:
        temp.append(data[i])
        idx.append(len(temp) - 1)
        continue
    temp[index] = data[i]
    idx.append(index)

check = len(temp) - 1
answer = []
for i in range(len(idx) - 1, -1, -1):
    if idx[i] == check:
        check -= 1
        answer.append(data[i])

answer.reverse()

print(len(answer))
for i in answer:
    print(i, end=" ")