def solution(record):
    answer = []
    dic = {}
    log = []
    for i in record:
        data = i.split()
        if len(data) == 3:
            dic[data[1]] = data[2]
        if data[0] == 'Enter':
            log.append(data[1]+"님이 들어왔습니다.")
        if data[0] == 'Leave':
            log.append(data[1]+"님이 나갔습니다.")
    for i in log:
        data = i.split("님")
        answer.append(dic[data[0]]+"님"+data[1])
    return answer