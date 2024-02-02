from collections import deque

for test_case in range(1, 11):
    n = int(input().rstrip())
    data = list(map(int, input().split()))
    queue = deque(data)
    index = 1
    while True:
        a = queue.popleft()
        a -= index
        if a <= 0:
            queue.append(0)
            break
        else:
            queue.append(a)
            index += 1
            if index >= 6:
                index = 1
    print("#" + str(test_case), end=" ")
    for i in queue:
        print(i, end=" ")
    print()