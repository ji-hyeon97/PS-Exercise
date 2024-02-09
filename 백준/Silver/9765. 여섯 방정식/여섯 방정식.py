import sys
import math

c1, c2, c3, c4, c5, c6 = map(int, sys.stdin.readline().split())


def prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num != i and num % i == 0:
            return i, num // i


x1, x2, x3, x5, x6, x7 = 0, 0, 0, 0, 0, 0
for i in prime(c1):
    for j in prime(c5):
        if i == j:
            x2 = i

x1 = c1 // x2
x3 = c5 // x2

for i in prime(c3):
    for j in prime(c6):
        if i == j:
            x6 = i
x5 = c6 // x6
x7 = c3 // x6
print(x1, x2, x3, x5, x6, x7)