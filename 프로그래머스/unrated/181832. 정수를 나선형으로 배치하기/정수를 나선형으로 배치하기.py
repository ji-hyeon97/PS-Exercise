def solution(n):
    answer = [[0] * n for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    r, c = 0, 0
    d = 1
    k = n * n
    cnt = 1
    while True:
        if cnt >= k:
            break
        nx = r + dx[d]
        ny = c + dy[d]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or answer[nx][ny] != 0:
            d = (d + 1) % 4
            continue
        answer[r][c] = cnt
        cnt += 1
        r = nx
        c = ny
    answer[r][c] = k
    return answer