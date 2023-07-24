def solution(ingredient):
    answer = 0
    data = ""
    stack=[]
    cnt = 0
    while True:
        if cnt == len(ingredient):
            break
        for i in ingredient:
            stack.append(i)
            cnt+=1
            if len(stack)>=4 and stack[-1] ==1 and stack[-2] ==3 and stack[-3] ==2 and stack[-4] ==1:
                for _ in range(4):
                    stack.pop()
                answer+=1
    return answer