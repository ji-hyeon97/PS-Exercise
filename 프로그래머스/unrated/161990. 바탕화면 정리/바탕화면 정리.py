def solution(wallpaper):
    answer = []
    data = []
    first = 0
    second = 0
    third = 0
    fourth = 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                data.append((i,j))
    data.sort()
    first = data[0][0]
    third = data[-1][0]+1
    data.sort(key=lambda v:v[1])
    second = data[0][1]
    fourth = data[-1][1] +1
    answer = [first,second,third,fourth]
    return answer