import sys
import math

data = [0 for i in range(1000001)]


for j in range(3, 1000001, 2):
    target = int(math.sqrt(j)) + 1
    health = 0
    for i in range(2, target):
        if j % i == 0:
            health = 1
            break
    if health == 0:
        data[j] = 1


while True:
    n = int(sys.stdin.readline().rstrip())

    check = 0
    if n == 0:
        break

    for i in range(3, n + 1, 2):
        if data[i] == 1:
            if data[n - i] == 1 and (n - i) > 2:
                print(str(n) + " = " + str(i) + " + " + str(n - i))
                check = 1
                break
    if check == 0:
        print("Goldbach's conjecture is wrong.")