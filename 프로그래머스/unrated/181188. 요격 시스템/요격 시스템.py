def solution(targets):
    answer = 0
    targets.sort(key=lambda v:v[1])
    shoot = -1
    for a,b in targets:
        if a>=shoot:
            shoot = b-0.1
            answer+=1
    return answer