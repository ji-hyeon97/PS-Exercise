import sys
from itertools import permutations

n,m = map(int,sys.stdin.readline().split())
data=[]
for i in range(n):
  data.append(i+1)
  
for i in permutations(data,m):
  i = str(i).replace("(","")
  i = i.replace(")","")
  i = i.replace(",","")
  print(i)