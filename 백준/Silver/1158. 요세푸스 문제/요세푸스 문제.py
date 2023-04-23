import sys

n, k = map(int, sys.stdin.readline().split())
data = []
check = [0 for _ in range(n)]

for i in range(1, n + 1):
    data.append(i)

count = 0
index = 0
result = []
while True:
    if len(result) == n:
        break

    if check[index] == 0:
        count += 1
        if count == k:
            check[index] = 1
            count = 0
            result.append(data[index])
    index += 1

    if index >= n:
        index = index % n

answer = '<'
for i in result:
    answer += str(i)
    if i == result[-1]:
        answer += ">"
    else:
        answer += ", "

print(answer)