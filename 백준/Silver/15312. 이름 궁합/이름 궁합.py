import sys
from collections import deque

queue = deque()

man = sys.stdin.readline().rstrip()
woman = sys.stdin.readline().rstrip()
nums = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

for i in range(len(man)):
    queue.append(nums[ord(man[i]) - 65])
    queue.append(nums[ord(woman[i]) - 65])

answer = deque()
while True:
    temp = []
    if len(answer) == 2:
        break
    for i in range(len(queue) - 1):
        target = (queue[i] + queue[i + 1]) % 10
        temp.append(target)
    queue = deque(temp)
    answer = deque(temp)
if answer[0] == 0:
    print('0' + str(answer[1]))
else:
    result = 10 * answer[0] + answer[1]
    print(result)