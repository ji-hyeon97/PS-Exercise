def solution(triangle):
    answer = 0
    for i in range(1,len(triangle)):
        for j in range(i+1):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            if j == i:
                triangle[i][j] += triangle[i-1][j-1]
            if 0<j and j<i:
                triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j])     
    return max(triangle[-1])