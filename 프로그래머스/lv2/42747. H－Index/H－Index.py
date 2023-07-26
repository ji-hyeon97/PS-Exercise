def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    n = len(citations)
    
    h = citations[0]
    cnt = 0

    while True:
        for i in citations:
            if i>=h:
                cnt+=1
        if cnt >= h:
            answer = h
            break
        cnt = 0
        h = h-1 
    return answer