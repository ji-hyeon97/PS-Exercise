import sys

a,b = map(int,sys.stdin.readline().split())
dic1 = {}
dic2 = {}
for i in range(1,a+1):
    character = sys.stdin.readline().rstrip()
    dic1[str(i)] = character
    dic2[character] = i

for _ in range(b):
    question = sys.stdin.readline().rstrip()
    if question in dic1:
        print(dic1[question])
    else:
        print(dic2[question])