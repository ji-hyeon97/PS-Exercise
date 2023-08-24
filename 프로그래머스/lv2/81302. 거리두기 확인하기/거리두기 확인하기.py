import collections
def solution(places):
    answer = []
    for data in places:
        developers = []
        flag = 1
        for i in range(5):
            for j in range(5):
                if data[i][j] == 'P':
                    developers.append((i,j))
        for i in range(len(developers)-1):
            for j in range(i+1,len(developers)):
                one,two = developers[i]
                three,four = developers[j]
                a = max(one,three)
                b = min(one,three)
                c = max(two,four)
                d = min(two,four)
                dic = collections.defaultdict(int)
                if abs(one-three) + abs(two-four) <=2:
                    for i1 in range(b,a+1):
                        for j2 in range(d,c+1):
                            dic[data[i1][j2]]+=1
                    if 'O' in dic or len(dic) == 1:
                        flag = 0
                        answer.append(0)
                        break
            if flag == 0:
                break
        if flag == 1:
            answer.append(1)           
    return answer