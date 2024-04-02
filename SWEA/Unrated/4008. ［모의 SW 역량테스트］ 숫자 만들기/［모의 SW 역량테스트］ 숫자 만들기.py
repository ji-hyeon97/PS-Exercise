T = int(input().rstrip())


def dfs(plus, minus, multiply, divide, index, value):
    global result1, result2
    if index == len(data):
        result1 = min(result1, value)
        result2 = max(result2, value)
        return

    if plus > 0:
        temp = value + data[index]
        dfs(plus - 1, minus, multiply, divide, index + 1, temp)

    if minus > 0:
        temp = value - data[index]
        dfs(plus, minus - 1, multiply, divide, index + 1, temp)

    if multiply > 0:
        temp = value * data[index]
        dfs(plus, minus, multiply - 1, divide, index + 1, temp)

    if divide > 0:
        if data[index] == 0:
            return
        if value < 0:
            temp = int(value / data[index])
        else:
            temp = int(value / data[index])
        dfs(plus, minus, multiply, divide - 1, index + 1, temp)


for t in range(1, T + 1):
    N = int(input().rstrip())
    plus1, minus1, multiply1, divide1 = map(int, input().split())
    result1 = int(1e9)
    result2 = -1 * int(1e9)
    data = list(map(int, input().split()))
    dfs(plus1, minus1, multiply1, divide1, 1, data[0])
    print("#" + str(t) + " " + str(result2 - result1))
