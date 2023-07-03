def solution(s):
    
    array = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in array:
        if i in s:
            s=s.replace(i,str(array.index(i)))
    answer = int(s)
    return answer