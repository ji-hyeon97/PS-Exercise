import sys

n = int(sys.stdin.readline().rstrip())


def fact(node):
    if node == 0:
        return 1
    if node == 1:
        return 1

    return node * fact(node - 1)


for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    answer = int(fact(b) / (fact(a) * fact(b - a)))
    print(answer)