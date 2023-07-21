answer = 0
def DFS(k,dungeons,ch,cnt):
    global answer
    answer = max(answer,cnt)
    for i in range(len(dungeons)):
        if k>=dungeons[i][0] and ch[i] ==0:
            ch[i] = 1
            DFS(k-dungeons[i][1],dungeons,ch,cnt+1)
            ch[i] = 0

def solution(k, dungeons):
    global answer
    ch = [0] * (len(dungeons)+5)
    DFS(k,dungeons,ch,0)
    return answer