import sys

n = int(sys.stdin.readline().rstrip())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

graph.sort(key=lambda v: v[0])
data = []
dic = {}
for a, b in graph:
    dic[b] = a
    data.append(b)

temp = [data[0]]
source = [0]


def lowerBound(target):
    left = 0
    right = len(temp) - 1
    mid = (left + right) // 2

    if target > temp[right]:
        return -1
    if target <= temp[left]:
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
        source.append(len(temp)-1)
        continue
    temp[index] = data[i]
    source.append(index)

print(n - len(temp))

standard = len(temp) - 1
for i in range(len(source) - 1, -1, -1):
    if source[i] == standard:
        standard -= 1
        del dic[data[i]]

for i in range(len(data)):
    if data[i] in dic:
        print(dic[data[i]])