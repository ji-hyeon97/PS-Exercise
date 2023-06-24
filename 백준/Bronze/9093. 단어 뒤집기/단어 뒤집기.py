import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    data = list(map(str, sys.stdin.readline().split()))
    answer = ""

    for i in data:
        for j in range(len(i)):
            answer += i[-j-1]
        answer += " "

    print(answer)