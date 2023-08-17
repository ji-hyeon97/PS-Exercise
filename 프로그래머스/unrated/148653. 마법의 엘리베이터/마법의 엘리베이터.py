def solution(storey):
    answer = 0
    while True:
        if storey == 0:
            break
        move = storey%10
        storey = storey//10
        if move<5:
            answer+=move
        if move>5:
            answer+=(10-move)
            storey+=1
        if move==5:
            if storey%10>=5:
                answer+=move
                storey+=1
            else:
                answer+=move
    return answer