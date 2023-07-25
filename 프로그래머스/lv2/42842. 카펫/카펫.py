def solution(brown, yellow):
    answer = []
    width = yellow + brown
    
    for i in range(3, width+1):
        row = i
        if width%row != 0:
            continue
        else:
            col = width//row
        if row == (brown+4-2*col)//2:
            break
    answer = [row,col]
    answer.sort(reverse=True)   
    return answer