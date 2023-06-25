import sys

n = int(sys.stdin.readline().rstrip())
answer = 1

for i in range(1, n + 1):
    answer *= i

data = reversed(str(answer))

count = 0
for i in data:
    if i == '0':
        count += 1
    else:
        break
print(count)