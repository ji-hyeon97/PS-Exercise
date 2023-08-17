import heapq
def solution(rows, columns, queries):
    answer = []
    graph = []
    temp = []
    for i in range(1,rows*columns+1):
        temp.append(i)
        if i%columns==0:
            graph.append(temp)
            temp = []
    for x1,y1,x2,y2 in queries:
        heap = []
        x1-=1
        y1-=1
        x2-=1
        y2-=1
        target = graph[x1][y1]
        for i in range(y1,y2):
            graph[x1][i+1],target = target,graph[x1][i+1]
            heapq.heappush(heap,target)
        for i in range(x1,x2):
            graph[i+1][y2],target = target,graph[i+1][y2]
            heapq.heappush(heap,target)
        for i in range(y2,y1,-1):
            graph[x2][i-1],target = target,graph[x2][i-1]
            heapq.heappush(heap,target)
        for i in range(x2,x1,-1):
            graph[i-1][y1],target = target,graph[i-1][y1]
            heapq.heappush(heap,target)
        answer.append(heap[0])
    return answer