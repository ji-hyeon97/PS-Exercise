from collections import deque

def solution(board):
    queue = deque()
    graph = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                queue.append((i,j))
                graph[i][j] = 1
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    
    def bfs():
        while queue:
            x,y = queue.popleft()
            if board[x][y] == 'G':
                return graph[x][y]
            for i in range(4):
                nx = x
                ny = y
                while True:
                    nx = nx+dx[i]
                    ny = ny+dy[i]
                    if nx<0 or ny<0 or nx>=len(board) or ny>=len(board[0]):
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                    if board[nx][ny] == 'D':
                        nx-=dx[i]
                        ny-=dy[i]
                        break
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx,ny))
        return -1             
    answer = bfs()
    if answer>0:
        answer -= 1    
    return answer