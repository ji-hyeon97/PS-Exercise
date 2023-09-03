import sys

n,m = map(int,sys.stdin.readline().split())
result = []

def backTracking(start):
  if len(result) == m:
    for i in range(m):
      print(result[i], end=" ")
    print("")
    return
  for i in range(start,n+1):
    result.append(i)
    backTracking(i)
    result.pop()

backTracking(1)