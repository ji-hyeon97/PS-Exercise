import sys
import math

n = int(sys.stdin.readline().rstrip())
dic = []


def isPrime(num):
    for i in range(2, int(math.sqrt(num))+2):
        if num % i == 0:
            return 0
    return 1


for i in range(2, int(math.sqrt(n)) + 1):
    check = {}
    while True:
        if n % i == 0:
            check[i] = 1
            dic.append(i)
            n = n // i
            if n == 1:
                break
            if isPrime(n):
                if n in check:
                    continue
                dic.append(n)
                n = 1
        else:
            break
if len(dic) == 0:
    dic.append(n)
print(len(dic))
for i in dic:
    print(i, end=" ")