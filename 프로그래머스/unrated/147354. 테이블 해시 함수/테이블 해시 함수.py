def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x:(x[col-1],-x[0]))
    temp = []
    for i in range(row_begin-1,row_end):
        value = 0
        for j in data[i]:
            value += j%(i+1)
        temp.append(value)  
    answer = temp[0]
    for i in range(1,len(temp)):
        answer=answer^temp[i]
    return answer