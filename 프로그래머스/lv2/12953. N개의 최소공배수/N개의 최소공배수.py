import math

def solution(arr):
    answer = 0
    while(True):
        if len(arr) == 1:
            break
        data1 = arr.pop()
        data2 = arr.pop()
        data3 = math.gcd(data1,data2)
        data = (data1 * data2) // data3
        arr.append(data)
    answer = arr[0]
    return answer