def solution(n, m, section):
    answer = 0
    
    check = [1] * (n+1)
    
    for i in section:
        check[i] = 0
      
    i = 0
    while (i<n+1):
        if check[i] == 0:
            check[i] = 1
            i = i+m
            answer+=1
        else:
            i +=1
        
    return answer