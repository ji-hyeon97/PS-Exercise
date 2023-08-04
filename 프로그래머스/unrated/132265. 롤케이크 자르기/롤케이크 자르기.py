import collections

def solution(topping):
    answer = 0
    left = collections.defaultdict(int)
    right = collections.defaultdict(int)
    for i in topping:
        right[i]+=1
    for i in topping:
        left[i]+=1
        if right[i]>1:
            right[i]-=1
        else:
            del right[i]
        if len(left) == len(right):
            answer+=1
    return answer