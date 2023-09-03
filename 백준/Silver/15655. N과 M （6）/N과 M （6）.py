import sys

n,m  = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))
data.sort()
result= []

def backTracking(start):
  if len(result) == m:
    for i in range(m):
      print(result[i], end=" ")
    print("")
    return
  for i in range(start, len(data)):
    if data[i] not in result:
      result.append(data[i])
      backTracking(i)
      result.pop()
backTracking(0)