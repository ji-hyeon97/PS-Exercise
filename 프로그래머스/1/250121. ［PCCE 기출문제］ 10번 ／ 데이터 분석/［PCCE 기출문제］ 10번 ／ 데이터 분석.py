def solution(data, ext, val_ext, sort_by):
    answer = []
    dic = {"code":0, "date":1, "maximum":2, "remain":3}
    
    data.sort(key=lambda v:(v[dic[sort_by]]))
    
    for i in data:
        if i[dic[ext]] < val_ext:
            answer.append(i)
    
    return answer