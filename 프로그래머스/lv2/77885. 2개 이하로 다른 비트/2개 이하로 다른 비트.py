def solution(numbers):
    answer = []
    for i in numbers:
        if i%2 == 0:
            answer.append(i+1)
        else:
            data = bin(i).replace("0b","")
            if '0' not in data:
                data = '0'+data
            temp = []
            for j in data:
                temp.append(j)
            for i in range(len(temp)-1,-1,-1):
                if temp[i] == '0':
                    temp[i] = '1'
                    temp[i+1] = '0'
                    break
            result = '0b'
            for i in temp:
                result+=i
            target = int(result,2)
            answer.append(target)               
    return answer