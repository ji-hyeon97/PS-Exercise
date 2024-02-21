from itertools import combinations

T = int(input().rstrip())

for t in range(1, T + 1):
    n = int(input().rstrip())
    graph = []
    for _ in range(n):
        data = list(map(int, input().split()))
        graph.append(data)

    left_combinations = list(combinations(range(n), n // 2))

    flavor = int(1e9)

    for left in left_combinations:
        right = set(range(n)) - set(left)

        leftValue = 0
        for x, y in combinations(left, 2):
            leftValue += graph[x][y] + graph[y][x]

        rightValue = 0
        for x, y in combinations(right, 2):
            rightValue += graph[x][y] + graph[y][x]

        flavor = min(flavor, abs(leftValue - rightValue))

    print("#" + str(t) + " " + str(flavor))