from collections import deque

T = int(input().rstrip())

for t in range(1, T + 1):
    n, k = map(int, input().split())
    data = input().rstrip()
    queue = deque(data)
    length = n // 4
    possible = []
    index = 0
    while True:
        if index == length:
            break
        temp = ""
        for i in range(len(queue)):
            temp += queue[i]
            if len(temp) == length:
                possible.append(temp)
                temp = ""

        a = queue.pop()
        queue.appendleft(a)
        index += 1
    dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
           'D': 13,
           'E': 14, 'F': 15}

    result = []
    for data in possible:
        temp = 0
        for i in range(length):
            temp += (16 ** i) * dic[data[length - i - 1]]
        result.append(temp)
    result = list(set(result))
    result.sort(reverse=True)

    print("#" + str(t) + " " + str(result[k - 1]))