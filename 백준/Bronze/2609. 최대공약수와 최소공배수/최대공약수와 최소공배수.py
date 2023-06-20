import sys
import math

a, b = map(int, sys.stdin.readline().split())
gcd = math.gcd(a, b)
lcm = int(a * b / gcd)

print(gcd)
print(lcm)