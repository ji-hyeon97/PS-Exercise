import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    data = list(map(int, sys.stdin.readline().split()))
    target_value = data[m]
    target_index = m + 1

    queue = deque()
    max_value = float('-inf')

    for i in range(len(data)):
        value = data[i]
        queue.append((value, i + 1))
        if value > max_value:
            max_value = value

    answer = 0

    while queue:
        current_value, current_index = queue.popleft()

        if current_value < max_value:
            queue.append((current_value, current_index))
        else:
            answer += 1
            if current_index == target_index:
                print(answer)
                break
            if current_value == max_value:
                max_value = float('-inf')
                for value, _ in queue:
                    if value > max_value:
                        max_value = value