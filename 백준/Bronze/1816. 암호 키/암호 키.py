import sys

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    flag = 1
    for i in range(2,1000001):
        if num%i == 0:
            flag = 0
            print("NO")
            break
    if flag == 1:
        print("YES")