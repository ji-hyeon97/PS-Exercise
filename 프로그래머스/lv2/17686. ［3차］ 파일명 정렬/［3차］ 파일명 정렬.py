def solution(files):
    numbers = [str(i) for i in range(10)]
    temp = []
    answer = []
    for file in files:
        head = ''
        number = ''
        tail = ''
        flag = 1
        second = 1
        for i in file:
            if flag == 1 and i not in numbers:
                head+=i
                continue
            flag = 0
            if second == 1 and i in numbers:
                number+=i
                continue
            else:
                second = 0
                tail+=i
        temp.append([head,number,tail])
    temp.sort(key=lambda v:(v[0].upper(),int(v[1])))
    for data in temp:
        value = ""
        for i in data:
            value+=i
        answer.append(value)
    return answer