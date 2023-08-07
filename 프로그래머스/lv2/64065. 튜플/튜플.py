def solution(s):
    answer = []
    s=s.replace('{{',"")
    s=s.replace("}}","")
    s=s.replace("},{"," ")
    data = s.split(" ")
    data.sort(key=len)
    check = [0] * 100010
    dic = {}
    for i in data:
        element = i.split(",")
        for j in element:
            if check[int(j)] == 1:
                continue
            answer.append(int(j))
            check[int(j)] = 1
    return answer