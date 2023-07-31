from collections import deque
import math

def solution(n, k):
    data = ''
    answer = 0
    queue = deque()
    while True:
        if n==0:
            break
        queue.appendleft(str(n%k))
        n = n//k
    for i in queue:
        data+=i
    num = data.split("0")
    for i in num:
        if i == '' or i == '1':
            continue
        mid = int(math.sqrt(int(i)))+1
        flag = 1
        for j in range(2,mid):
            if int(i)%j==0:
                flag = 0
                break
        if flag == 1:
            answer+=1
    return answer