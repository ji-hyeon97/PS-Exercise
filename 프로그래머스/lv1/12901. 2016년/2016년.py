def solution(a, b):
    answer = ''
    dict = {}
    dict[0] = 0
    dict[1] = 31
    dict[2] = dict[1]+29
    dict[3] = dict[2]+31
    dict[4] = dict[3]+30
    dict[5] = dict[4]+31
    dict[6] = dict[5]+30
    dict[7] = dict[6]+31
    dict[8] = dict[7]+31
    dict[9] = dict[8]+30
    dict[10] = dict[9]+31
    dict[11] = dict[10]+30
    dict[12] = dict[11]+31
    
    day = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    target = dict[a-1]+b
    print(day[((target%7)+4)%7])
    answer = day[((target%7)+4)%7]
    
    return answer