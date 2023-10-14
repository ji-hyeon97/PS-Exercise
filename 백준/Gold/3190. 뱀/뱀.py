import sys

n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())
apple = [tuple(map(int, sys.stdin.readline().split())) for _ in range(k)]
l = int(sys.stdin.readline().rstrip())
data = [sys.stdin.readline().split() for _ in range(l)]
dtbl = [0] * 10001

for sec, turn in data:
    dtbl[int(sec)] = turn

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
dr = 1
snake = [(1, 1)]
answer = 0

while True:
    answer += 1
    ci, cj = snake[0]
    ni, nj = ci + di[dr], cj + dj[dr]

    if 1 <= ni <= n and 1 <= nj <= n and (ni, nj) not in snake:
        snake.insert(0, (ni, nj))
        if (ni, nj) in apple:
            apple.remove((ni, nj))
        else:
            snake.remove(snake[-1])
        if dtbl[answer] == 'D':
            dr = (dr + 1) % 4
        elif dtbl[answer] == 'L':
            dr = (dr + 3) % 4
    else:
        break
print(answer)