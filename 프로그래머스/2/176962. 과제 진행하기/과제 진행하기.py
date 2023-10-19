from collections import deque


def solution(plans):
    answer = []
    data = []
    queue = deque()
    for subject, start, finish in plans:
        h, m = start.split(":")
        start = int(h) * 60 + int(m)
        finish = int(finish)
        data.append([subject, start, finish])
    data.sort(key=lambda v: v[1])
    for i in range(len(data)):
        if i == len(data) - 1:
            answer.append(data[i][0])
            continue
        if data[i][1] + data[i][2] <= data[i + 1][1]:
            answer.append(data[i][0])
            freeTime = data[i + 1][1] - data[i][2] - data[i][1]
            while True:
                if len(queue) == 0:
                    break
                subject, start, left = queue.pop()
                if freeTime >= left:
                    freeTime -= left
                    answer.append(subject)
                else:
                    queue.append([subject, start, left - freeTime])
                    break
        else:
            data[i][2] = data[i][2] - (data[i + 1][1] - data[i][1])
            queue.append(data[i])
    while True:
        if len(queue) == 0:
            break
        subject = queue.pop()
        answer.append(subject[0])
    return answer