def solution(board, moves):
    answer = 0
    box = []
    height = len(board)
    
    for i in moves:
        for j in range(height):
            if board[j][i-1] != 0:
                if box and box[-1] == board[j][i-1]:
                    box.pop()
                    answer+=2
                else:
                    box.append(board[j][i-1])
                board[j][i-1] = 0
                break
    return answer