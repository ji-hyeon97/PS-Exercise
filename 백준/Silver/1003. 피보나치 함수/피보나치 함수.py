import sys

t = int(sys.stdin.readline().rstrip())
zero = [1,0,1]
one = [0,1,1]

def fib(n):
  if n>=3:
    for i in range(2,n):
      zero.append(zero[i]+zero[i-1])
      one.append(one[i]+one[i-1])
  print(zero[n], one[n])
  

for _ in range(t):
  n = int(sys.stdin.readline().rstrip())
  fib(n)
  zero = [1,0,1]
  one = [0,1,1]