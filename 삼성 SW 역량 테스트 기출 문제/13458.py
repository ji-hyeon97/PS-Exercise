import sys

n = int(sys.stdin.readline().rstrip())
student = list(map(int,sys.stdin.readline().split()))
main, sub = map(int,sys.stdin.readline().split())

data = []
for i in student:
  data.append(i-main)

answer = n
for i in data:
  if i>0:
    if i%sub == 0:
      answer+=int(i//sub)
    else:
      answer+=int(i//sub)+1
print(answer)
    