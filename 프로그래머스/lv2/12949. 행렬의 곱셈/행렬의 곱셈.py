def solution(arr1, arr2):
    row = len(arr1)
    col = len(arr2[0])
    answer = [[] for _ in range(row)]
    
    for i in range(row):
        for j in range(len(arr2[0])):
            data = 0
            for k in range(len(arr2)):
                data += arr1[i][k] * arr2[k][j]
            answer[i].append(data)
    return answer