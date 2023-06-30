def solution(lottos, win_nums):
    answer = []
    big = 0
    small = 0
    
    for i in lottos:
        if i == 0:
            big+=1
            continue
        if i in win_nums:
            big+=1
            small+=1
            
    big = 7-big
    small = 7-small
    
    if small == 7:
        small = 6
    if big == 7:
        big = 6
    
    answer = [big,small]
    return answer