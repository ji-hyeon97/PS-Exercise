import sys

n, m = map(int, sys.stdin.readline().split())


def two(number):
    answer = 0
    while number >= 2:
        answer += int(number / 2)
        number = int(number / 2)
    return answer


def five(number):
    answer = 0
    while number >= 5:
        answer += int(number / 5)
        number = int(number / 5)
    return answer


up = five(n) - five(n - m) - five(m)
down = two(n) - two(n - m) - two(m)
print(min(up, down))