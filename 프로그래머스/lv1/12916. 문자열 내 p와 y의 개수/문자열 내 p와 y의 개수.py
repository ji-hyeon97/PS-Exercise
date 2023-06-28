def solution(s):
    answer = True
    pCount = 0
    yCount = 0
    for i in s:
        if i in ['P','p']:
            pCount+=1
        if i in ['Y','y']:
            yCount+=1
    if pCount!=yCount:
        answer = False
    return answer