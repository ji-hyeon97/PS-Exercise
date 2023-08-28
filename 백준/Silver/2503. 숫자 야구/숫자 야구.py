import sys
import collections

n = int(sys.stdin.readline().rstrip())
data = []
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))
dic = collections.defaultdict(int)
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if a == b or b == c or c == a:
                continue
            for i in data:
                strikeCounts = 0
                ballCounts = 0
                strike = i[1]
                ball = i[2]
                value = str(i[0])
                idx = 0
                for j in value:
                    if idx == 0:
                        if int(j) == a:
                            strikeCounts += 1
                        if int(j) == b or int(j) == c:
                            ballCounts += 1
                        idx += 1
                        continue
                    if idx == 1:
                        if int(j) == b:
                            strikeCounts += 1
                        if int(j) == a or int(j) == c:
                            ballCounts += 1
                        idx += 1
                        continue
                    if idx == 2:
                        if int(j) == c:
                            strikeCounts += 1
                        if int(j) == b or int(j) == a:
                            ballCounts += 1
                if strikeCounts == strike and ballCounts == ball:
                    dic[100 * a + 10 * b + c] += 1
answer = 0
for i in dic:
    if dic[i] == n:
        answer += 1
print(answer)