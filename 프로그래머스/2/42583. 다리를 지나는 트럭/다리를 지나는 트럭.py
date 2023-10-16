from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    finish = []
    passing = deque()
    total = len(truck_weights)
    wait = deque(truck_weights)
    onWeight = 0

    while True:
        if len(finish) == total:
            return answer
        if len(passing) != bridge_length:
            if len(wait) > 0:
                car = wait[0]
                if onWeight + car > weight:
                    passing.append(0)
                else:
                    onWeight += car
                    car = wait.popleft()
                    passing.append(car)
            else:
                passing.append(0)
        else:
            exits = passing.popleft()
            if exits != 0:
                finish.append(exits)
                onWeight -= exits
            if len(wait) > 0:
                car = wait[0]
                if onWeight + car > weight:
                    passing.append(0)
                else:
                    car = wait.popleft()
                    passing.append(car)
                    onWeight += car
            else:
                passing.append(0)
        answer += 1