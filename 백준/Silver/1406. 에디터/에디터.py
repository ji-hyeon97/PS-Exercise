import sys

data = list(map(str, sys.stdin.readline().rstrip()))
another = []

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    command = list(map(str, sys.stdin.readline().split()))
    if command[0] == 'P':
        data.append(command[1])
    elif command[0] == 'L' and data:
        another.append(data.pop())
    elif command[0] == 'D' and another:
        data.append(another.pop())
    elif command[0] == 'B' and data:
        data.pop()

print("".join(data+list(reversed(another))))