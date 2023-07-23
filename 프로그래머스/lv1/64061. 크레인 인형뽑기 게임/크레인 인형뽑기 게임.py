def solution(board, moves):
    answer = 0
    stack = []
    for idx in moves:
        idx = idx-1
        for i in range(len(board)):
            if len(stack) and stack[-1] == board[i][idx]:
                board[i][idx] = 0
                stack.pop()
                answer+=2
                break
            if board[i][idx] != 0:
                stack.append(board[i][idx])
                board[i][idx] = 0
                break
    return answer