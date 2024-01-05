from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    n,k = map(int,input().split())
    data = list(map(str,input().rstrip()))
    queue = deque(data)
    dic = {}
    for i in range(10):
        dic[str(i)] = i
    dic['A'] = 10
    dic['B'] = 11
    dic['C'] = 12
    dic['D'] = 13
    dic['E'] = 14
    dic['F'] = 15
    answer = []
    length = n//4

    for _ in range(len(data)):
        for i in range(0,n,length):
            temp = ""
            for j in range(length):
                temp+=queue[i+j]
            answer.append(temp)
        a = queue.popleft()
        queue.append(a)

    answer = list(set(answer))

    result = []
    for data in answer:
        temp = 0
        for i in range(len(data)):
            temp+=dic[data[i]]* (16**(len(data)-(i+1)))
        result.append(temp)
    result.sort(reverse=True)
    print("#"+str(test_case)+" "+str(result[k-1]))