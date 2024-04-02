T = int(input().rstrip())


def recur(index, total):
    global answer

    if index == n:
        if total < b:
            return
        answer = min(answer, total - b)
        return

    recur(index + 1, total)
    recur(index + 1, total + data[index])


for t in range(1, T + 1):
    n, b = map(int, input().split())
    data = list(map(int, input().split()))
    answer = int(1e9)
    recur(0, 0)
    print("#" + str(t) + " " + str(answer))