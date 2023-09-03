import sys

a, b = map(int, sys.stdin.readline().split())

data = []


def recur(data):
    if len(data) == b:
        for i in data:
            print(i, end=" ")
        print("")
        return
    else:
        for i in range(1, a + 1):
            if i not in data and i > max(data):
                data.append(i)
                recur(data)
                data.pop()


for i in range(1, a + 1):
    data.append(i)
    recur(data)
    data = []