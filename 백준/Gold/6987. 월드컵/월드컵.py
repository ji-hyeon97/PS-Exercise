import sys

match = []
check = [0 for _ in range(7)]
dic = {}


def comb(plist):
    global match
    if len(plist) == 2:
        tmp = tuple(sorted(plist))
        if tmp not in dic:
            dic[tmp] = 1
            match.append(plist)
            return
    for i in range(6):
        if check[i] == 0:
            check[i] = 1
            comb(plist + [i])
            check[i] = 0


comb([])


def dfs(count, win, draw, loss):
    global answer
    if count == 15:
        if win.count(0) == 6 and draw.count(0) == 6 and loss.count(0) == 6:
            answer = 1
        return

    home, away = match[count]
    if win[home] > 0 and loss[away] > 0:
        win[home] -= 1
        loss[away] -= 1
        dfs(count + 1, win, draw, loss)
        win[home] += 1
        loss[away] += 1

    if draw[home] > 0 and draw[away] > 0:
        draw[home] -= 1
        draw[away] -= 1
        dfs(count + 1, win, draw, loss)
        draw[home] += 1
        draw[away] += 1

    if loss[home] > 0 and win[away] > 0:
        loss[home] -= 1
        win[away] -= 1
        dfs(count + 1, win, draw, loss)
        loss[home] += 1
        win[away] += 1


for _ in range(4):
    data = list(map(int, sys.stdin.readline().split()))
    win = []
    draw = []
    loss = []
    for j in range(0, 16, 3):
        win.append(data[j])
        draw.append(data[j + 1])
        loss.append(data[j + 2])
    answer = 0
    dfs(0, win, draw, loss)
    print(answer, end=" ")