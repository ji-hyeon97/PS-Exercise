import sys

n = int(sys.stdin.readline().rstrip())
students = list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())
answer = 0

for i in students:
    i -= b
    answer += 1
    if i <= 0:
        continue
    if i % c == 0:
        answer += i // c
    else:
        answer += i // c + 1
print(answer)