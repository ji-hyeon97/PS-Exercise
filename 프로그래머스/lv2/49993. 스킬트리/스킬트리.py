def solution(skill, skill_trees):
    answer = 0
    for data in skill_trees:
        temp = ""
        dic = {}
        for i in data:
            if i in skill:
                temp+=i
        if skill == temp:
            answer+=1
        part = ""
        for i in skill:
            if part == temp:
                answer+=1
                break
            part+=i
    return answer