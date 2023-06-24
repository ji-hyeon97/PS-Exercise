import sys

t = int(sys.stdin.readline().rstrip())
d = [0] * (100)

d[1] = 1
d[2] = 2
d[3] = 4

for _ in range(t):
  n = int(sys.stdin.readline().rstrip())

  for i in range(4,n+1):
    d[i] = d[i-1]+d[i-2]+d[i-3]

  print(d[n])