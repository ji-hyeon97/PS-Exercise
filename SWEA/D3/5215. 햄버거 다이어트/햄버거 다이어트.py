test_case = int(input())

for i in range(test_case):
    n, l = map(int, input().split())
    graph = []
    for _ in range(n):
        data = list(map(int, input().split()))
        graph.append(data)
    answer = 0


    def eat(depth, score, kcal):
        global answer
        if kcal > l:
            return
        answer = max(answer, score)
        if depth >= n:
            return
        eat(depth + 1, score, kcal)
        eat(depth + 1, score + graph[depth][0], kcal + graph[depth][1])


    eat(0, 0, 0)
    print("#" + str(i + 1) + " " + str(answer))