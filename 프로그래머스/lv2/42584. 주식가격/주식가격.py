def solution(prices):
    answer = []
    idx = 0
    for i in range(len(prices)):
        time = 0
        idx = i
        data = prices[i]
        while True:
            if idx >= len(prices)-1:
                break
            if data>prices[idx]:
                break
            idx+=1
            time+=1
        answer.append(time)
    return answer