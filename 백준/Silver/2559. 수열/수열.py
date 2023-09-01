import sys

n,k = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

new=[]
count = 0
total = 0

for i in range(n):
  total+=data[i]
  count+=1
  if count == k:
    new.append(total)
    count-=1
    total-=data[i-k+1]
    
print(max(new))