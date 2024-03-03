import sys

n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))
data.sort()

answer = int(1e9) * 3

left = 0
right = n - 1
one, two = 0, 0
while True:
    if left == right:
        break

    if abs(0 - answer) > abs(0-(data[left] + data[right])):
        one = data[left]
        two = data[right]
        answer = data[left] + data[right]

    if data[left] + data[right] < 0:
        left += 1
    elif data[left] + data[right] > 0:
        right -= 1
    else:
        break

print(one, two)