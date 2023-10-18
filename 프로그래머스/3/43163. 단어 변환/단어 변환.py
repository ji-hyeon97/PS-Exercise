from collections import deque

def solution(begin, target, words):
    answer = 0
    queue = deque()
    queue.append((begin,0))
    check = [0 for _ in range(len(words))]
    
    while queue:
        word,cnt = queue.popleft()
        if word == target:
            answer = cnt
            break
        for i in range(len(words)):
            if check[i] == 0:
                temp = 0
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        temp+=1
                if temp == 1:
                    queue.append((words[i],cnt+1))
                    check[i] = 1
    return answer