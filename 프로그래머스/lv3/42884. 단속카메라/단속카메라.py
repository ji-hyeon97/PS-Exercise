def solution(routes):
    answer = 0
    target = -30001
    routes.sort(key=lambda v:v[1])
    for a,b in routes:
        if target<a:
            target = b
            answer+=1
    return answer