def solution(s, skip, index):
    answer = ''
    for i in s:
        cnt = 0
        check = ord(i)
        while True:
            if cnt == index:
                break
            check+=1
            if check > 122:
                check = 97
            if chr(check) not in skip:
                cnt+=1
        answer+=chr(check)
    return answer